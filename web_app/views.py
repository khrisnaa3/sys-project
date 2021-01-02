from django.http import HttpResponse
from django.shortcuts import render, redirect
import subprocess
from subprocess import Popen, PIPE, STDOUT


# Create your views here.

def index(request):
    return render(request, 'index.html')


def exec(request):
    # subprocess.call('./script/hello.sh')
    command = ["sh", "/home/stef/Documents/exec.sh"]
    try:
        process = Popen(command, stdout=PIPE, stderr=STDOUT)
        output = process.stdout.read()
        exitstatus = process.poll()
        if exitstatus == 0:
            result = {"status": "Success", "output": str(output)}
        else:
            result = {"status": "Failed", "output": str(output)}

    except Exception as e:
        result = {"status": "failed", "output": str(e)}
    html = """
    <!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

    <title>Kernel Bois</title>
</head>
<body>
<Container>
    <div style="text-align: center; margin: 2rem">
        <h1>Kernel Bois' Project</h1>
    </div>
    <div style="text-align: center; margin: 5rem">
        <div style="margin-bottom: 3rem">
            RESULT:
        </div>
        <div>
            Script status: %s <br>
            Output: %s <br>
        </div>
    </div>
</Container>

<!-- Optional JavaScript; choose one of the two! -->

<!-- Option 1: Bootstrap Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW"
        crossorigin="anonymous"></script>

<!-- Option 2: Separate Popper and Bootstrap JS -->
<!--
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js" integrity="sha384-q2kxQ16AaE6UbzuKqyBE9/u/KzioAlnx2maXQHiDX9d4/zp8Ok3f+M7DPm+Ib6IU" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-pQQkAEnwaBkjpqZ8RU1fF1AKtTcHJwFl3pblpTlHXybJjHpMYo79HY3hIi4NKxyj" crossorigin="anonymous"></script>
-->
</body>
</html>
    """ % (result['status'], result['output'])
    return HttpResponse(html)
