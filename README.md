# traffic-report

A command line report generator that connects to a PostgreSQL database for Udacity's news website.

## Usage
Run the traffic_report.py file in python to generate 3 reports based on the Udacity's news website database.
command: python traffic_report.py

## Report generation
3 reports are generated:
- three most popular articles
- most popular authors
- days with errors > %1


## Example output

The three most popular articles
title                                                   views
----------------------------------------
Candidate is jerk, alleges rival                       338647
Bears love berries, alleges bear                       253801
Bad things gone, say good people                       170098


The most popular authors
author                                                  views
----------------------------------------
Ursula La Multa                                        507594
Rudolf von Treppenwitz                                 423457
Anonymous Contributor                                  170098
Markoff Chaney                                          84557


Days with errors > %1
date                                                  % error
----------------------------------------
2016-07-17                                               2.26
