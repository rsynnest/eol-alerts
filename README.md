# EOL Alerts

This is a tool that aggregates End Of Life (EOL) dates from across the software/hardware industry and sends alerts for upcoming EOL software/hardware. Currently it is setup to run as a daily AWS lambda and sends alerts to a configurable Slack webhook.

## Dataset 

The base dataset is [this CIS EOS Report](https://www.cisecurity.org/wp-content/uploads/2020/07/EOS-Report-July-2020.pdf), which is a compilation of official company EOL reports from across the industry. Over time I hope to add some automation to pull data from official upstream sources and to prevent this CSV from exploding in size, but it works for now.

You can overwrite this CSV with your own entires to recieve only alerts relative to you, or you can submit a pull request to add EOL information for any publicly available software.

## Setup + Usage

1. Using the `.env.example` file as a reference, add your Slack Webhook URL to a `.env` file in the project root
2. Install + configure [serverless](https://www.serverless.com/) for your AWS Lambda instance
3. Run `sls deploy`


## Contributing

The simplest and most valuable contribution is to send a pull request to the `data/eos-report.csv` file with EOL information about a specific product.
The format for data being added to the file should be as follows:
`Company,Product,Version,EOL Date,Reference URL`
