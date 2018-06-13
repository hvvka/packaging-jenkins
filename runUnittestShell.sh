#!/usr/bin/env bash

find . -name "test_*.py" -print | while read f; do
        echo "$f"
        ###
        venv/bin/python3 -m coverage run "$f"
        venv/bin/python3 -m coverage xml -o coverage.xml
        ###
done

cp -r ./coverage.xml /Users/hg/.jenkins/workspace/jenkins_unit_tests/coverage.xml
cp -r ./python_unittests_xml /Users/hg/.jenkins/workspace/jenkins_unit_tests/python_unittests_xml
