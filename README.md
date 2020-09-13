# EOL Alerts

This is a tool that aggregates EOL information from across the software/hardware industry and sends out alerts for software/hardware that is going EOL in the next year, month, or day. Currently it is setup to run as a daily AWS lambda and sends alerts to a configurable Slack webhook URL.

The base dataset is [this CIS EOS Report](https://www.cisecurity.org/wp-content/uploads/2020/07/EOS-Report-July-2020.pdf), which is a compilation of official company EOL reports from across the industry. Over time I hope to add some automated data streams to official company sources. If you would like to contribute EOL data, please [see the "Contributing" section below](#contributing).

## Setup + Usage

1. Using the `.env.example` file as a reference, add your Slack Webhook URL to a `.env` file in the project root
2. Install + configure serverless for your AWS Lambda instance
3. Run `sls deploy`


## Justification

The eventual goal is to have a curated dataset of security and lifecycle information, as well as some basic tools for things like alerts and details. Hopefully this will ease some of the burden on managing complex software stacks and, focus security efforts across company divides. This is in the same vein as services like Github Dependabot, Microsoft updates, Debian/Ubuntu/OpenBSD/etc. security mailing lists, NIST, and CIS. But usually this information is spread out across these various companies. 

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
