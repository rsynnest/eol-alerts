# EOL Alerts

This is a tool for sending notifications on software/hardware that is going EOL.
The current data source is [this CIS EOS Report](https://www.cisecurity.org/wp-content/uploads/2020/07/EOS-Report-July-2020.pdf).
Over time I hope to be adding EOL data as I come across it.

## Behavior

Currently the script just sends Slack alerts to a provided Webhook URL.
It will send an alert on the first of the month listing any software that will be going EOL within the next month.
It will also send an alert on the day a specific software/hardware goes EOL.

## Setup + Usage

1. Using the `.env.example` file as a reference, add your Slack Webhook URL to a `.env` file in the project root

## Contributing

The simplest and most valuable contribution is to send a pull request to the `data/eos-report.csv` file with EOL information about a specific product.
Format for data being added should be:
`Provider,Product,Version,EOS Date,ReferenceURL`
