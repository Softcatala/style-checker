#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
#
# Copyright (c) 2021 Jordi Mas i Hernandez <jmas@softcatala.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.


from __future__ import print_function
import uvicorn
from fastapi import FastAPI, Form, Request
import json

import sys
sys.path.append('../core/')


from analyzer import Analyzer
from document import Document


app = FastAPI()


def json_answer(data, status = 200):
    json_data = json.dumps(data, indent=4, separators=(',', ': '))
    return json_data
#    resp = Response(json_data, mimetype='application/json', status = status)
#    resp.headers['Access-Control-Allow-Origin'] = '*'
#    return resp
   

@app.get('/metrics')
async def metrics_api(text: str):

#    text = request.args.get('text')
    document = Document(text)
    result = Analyzer(document).get_metrics()
    return result
#    return json_answer(result)

@app.route('/check', methods=['GET'])
def check_api():

    text = request.args.get('text')
    document = Document(text)
    result = Analyzer(document).get_all()
    return json_answer(result)


if __name__ == '__main__':
    uvicorn.run('style-service:app', host='0.0.0.0', port=5000)
