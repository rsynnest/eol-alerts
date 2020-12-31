# EOL Alerts

This is a tool that aggregates End Of Life (EOL) dates from across the software/hardware industry and sends alerts for upcoming EOL software/hardware. Currently it is setup to run as a daily AWS lambda and sends alerts to a configurable Slack webhook.

## Dataset 

The base dataset is [this CIS EOS Report](https://www.cisecurity.org/wp-content/uploads/2020/07/EOS-Report-July-2020.pdf), which is a compilation of official company EOL reports from across the industry. Over time I hope to add some automated data streams to official company sources. If you would like to contribute EOL data, please [see the "Contributing" section below](#contributing).

## Setup + Usage

1. Using the `.env.example` file as a reference, add your Slack Webhook URL to a `.env` file in the project root
2. Install + configure [serverless](https://www.serverless.com/) for your AWS Lambda instance
3. Run `sls deploy`


## Justification

As a sysadmin I have to keep up with a lot of different communication channels, usually mailing lists, to know what software/hardware is going EOL and when. In an ideal world, all patches are automated, and all software is maintained, and never goes out of date. But often legacy software going EOL requires major migration and planning. This tool is a simple way of having one place (in my case, a Slack channel) to track EOL information for all software/hardware I need to worry about. Unlike email, it's easy to add anyone to a single channel where they get all alerts and a searchable history. If this were to improve I could see a curated dataset of security and lifecycle information, as well as some basic tools for things like alerts and details, which could be shared across the industry. Each user could then subscribe to their desired software/hardware in one place, instead of going out and finding all necessary channels (many of which are not automatable, blog posts, etc). It's possible things like CVEs could be integrated at some point, but I'm keeping the scope minimal for now. Some similar services are Github Dependabot, Microsoft Updates, Debian/Ubuntu/OpenBSD/etc security mailing lists, NIST reports, and CIS reports.

## Todo

- [ ] Code cleanup

Improve/automate data sources:
 - [ ] Microsoft lifecycle exports: https://docs.microsoft.com/en-us/lifecycle/products/export
 - [ ] https://wiki.ubuntu.com/Releases
 - [ ] https://helpx.adobe.com/support/programs/eol-matrix.html
 - [ ] official sec-alert mailing lists
 - [ ] reach out to vendors for official data streams

Improve alerting
 - [ ] Implement an optional mailing list alert target
 - [ ] Implement a topic/subscription model for more targeted alerts on only relevant data sources


## Contributing

The simplest and most valuable contribution is to send a pull request to the `data/eos-report.csv` file with EOL information about a specific product.
The format for data being added to the file should be as follows:
`Company,Product,Version,EOL Date,Reference URL`
