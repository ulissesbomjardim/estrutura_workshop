// Shared approve-pr logic. Called by the workflow via actions/github-script.
// Exposes async function approvePR(github, context, core)
globalThis.approvePR = async (github, context, core) => {
  const rawBody = context.payload.comment && context.payload.comment.body ? context.payload.comment.body : '';
  core.info(`Comment body: "${rawBody}"`);

  const commenter = context.payload.comment && (context.payload.comment.user && context.payload.comment.user.login) ? context.payload.comment.user.login : context.actor;
  const association = context.payload.comment && context.payload.comment.author_association ? context.payload.comment.author_association : 'UNKNOWN';
  core.info(`Commenter: ${commenter}, association: ${association}`);

  const issueNumberMeta = context.payload.issue && context.payload.issue.number ? context.payload.issue.number : null;
  const commentId = context.payload.comment && context.payload.comment.id ? context.payload.comment.id : null;
  core.info(`Issue number: ${issueNumberMeta}, Comment id: ${commentId}`);

  const body = rawBody.replace(/\u00A0/g, ' ').trim();

  const owner = context.repo.owner;
  const repo = context.repo.repo;
  core.info(`Repository: ${owner}/${repo}`);

  const re = /(?:\/\s*)?approve-?pr[\s:\/\#-]*?(\d+)/i;
  let m = body.match(re);

  let prNumber = null;
  if (m) {
    prNumber = parseInt(m[1], 10);
  } else {
    core.info('No PR number found in comment, attempting to extract from issue title/body...');
    const issueTitle = context.payload.issue && context.payload.issue.title ? context.payload.issue.title : '';
    const issueBody = context.payload.issue && context.payload.issue.body ? context.payload.issue.body : '';
    core.info(`Issue title: "${issueTitle}"`);
    core.info(`Issue body (first 300 chars): "${issueBody.substring(0,300)}"`);
    const any = (issueTitle + '\n' + issueBody).match(/#(\d+)/);
    if (any) {
      prNumber = parseInt(any[1], 10);
      core.info(`Found PR number ${prNumber} in issue content.`);
    }
  }

  if (!prNumber) {
    core.setFailed('No PR number found in comment or issue. Use "/approve-pr #123" or include PR reference in the issue.');
    return;
  }

  try {
    const pr = await github.rest.pulls.get({ owner, repo, pull_number: prNumber });
    core.info(`Fetched PR #${prNumber}: title="${pr.data.title}", url=${pr.data.html_url}, state=${pr.data.state}`);
    if (typeof pr.data.mergeable !== 'undefined') {
      core.info(`PR.mergeable: ${pr.data.mergeable}`);
    }
    if (pr.data.merged) {
      core.info(`PR #${prNumber} already merged.`);
      return;
    }
  } catch (err) {
    core.setFailed(`Failed to get PR #${prNumber}: ${err.message}`);
    return;
  }

  try {
    const mergeRes = await github.rest.pulls.merge({ owner, repo, pull_number: prNumber, merge_method: 'squash' });
    core.info(`Merge response: ${JSON.stringify(mergeRes.data)}`);
    if (mergeRes.data && mergeRes.data.merged) {
      core.info(`PR #${prNumber} squashed and merged successfully.`);
    } else {
      core.setFailed(`PR #${prNumber} not merged: ${JSON.stringify(mergeRes.data)}`);
    }
  } catch (err) {
    core.setFailed(`Failed to squash-merge PR #${prNumber}: ${err.message}`);
  }
};
