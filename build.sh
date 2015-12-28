#!/bin/bash

cd documentation/
mkdocs build
mkdocs build --clean
cp -r site/* ../
cd -

