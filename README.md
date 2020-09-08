# EOL Alerts

This is a tool for sending notifications on software/hardware that is going EOL.
The current data source is [this CIS EOS Report](https://www.cisecurity.org/wp-content/uploads/2020/07/EOS-Report-July-2020.pdf).
Over time I hope to be adding EOL data as I come across it.

## Todo

Incorporate source data:
 - Microsoft lifecycle exports: https://docs.microsoft.com/en-us/lifecycle/products/export
 - https://wiki.ubuntu.com/Releases
 - https://helpx.adobe.com/support/programs/eol-matrix.html

## Behavior

Right now the script just sends Slack alerts to a provided Webhook URL.
It will send an alert on the first of the month listing any software that is going EOL within the next month.
It will also send an alert on the day a specific software/hardware goes EOL.

## Setup + Usage

1. Using the `.env.example` file as a reference, add your Slack Webhook URL to a `.env` file in the project root
2. Install + configure serverless for your AWS Lambda instance
3. Run `sls deploy`

## Contributing

The simplest and most valuable contribution is to send a pull request to the `data/eos-report.csv` file with EOL information about a specific product.
The format for data being added to the file should be as follows:
`Company,Product,Version,EOL Date,Reference URL`
