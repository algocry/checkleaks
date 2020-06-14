# Security Policy

1. [Reporting security problems to StrinTH](#reporting)
2. [Incident Response Process](#process)
3. [Vulnerability Management Plans](#vulnerability-management)

<a name="reporting"></a>
## Reporting security problems to WIP

**DO NOT CREATE AN ISSUE** to report a security problem. Instead, please
send an email to 0x0is1off@gmail.com

<a name="process"></a>
## Incident Response Process

In case an incident is discovered or reported, we will follow the following
process to contain, respond and remediate:

### 1. Containment

The first step is to find out the root cause, nature and scope of the incident.

- Is still ongoing? If yes, first priority is to stop it.
- Is the incident outside of my influence? If yes, first priority is to contain it.
- Find out knows about the incident and who is affected.
- Find out what data was potentially exposed.

### 2. Response

After the initial assessment and containment to my best abilities, we will
document all actions taken in a response plan.

### 3. Remediation

Once the incident is confirmed to be resolved, we will summarize the lessons
learned from the incident and create a list of actions we will take to prevent
it from happening again.

<a name="vulnerability-management"></a>
## Vulnerability Management Plans

### Keep permissions to a minimum

The checkleaks uses the least amount of access to limit the impact of possible
security incidents, see [Information collection and use](PRIVACY.md#information-collection-and-use).

If someone would get access to the checkleaks, the worst thing they could do is to
read out contents from pull requests, limited to repositories the checkleaks got
installed on.

### Secure accounts with access

The [StrinTH GitHub Organization](https://github.com/StrinTH) requires 2FA authorization
for all members.
