#This is tutorial project of django-comments-xtd. Also django-sockpuppet is added to this project to check how it works.


### To run this project you have to set up python and nodejs virtual enviroments.
One of good choises for managing virtual enviromens is Miniconda.
It supports having isolated python as well as nodejs enviroments. 
- Install miniconda on your Linux machine.
- Create conda environment from file: `conda env create -f environment.yml`
- Activate virtual enviroment: `conda activate env38_python_nodejs`
- Check python version: `python --version`
- Check nodejs version: `node --version`

Now you can install all required nodejs dependencies for the project (node_modules):

- `npm install`

Now you have single working isolated environment for developing application with both django and nodejs.

Webpack is configured to build static only. Django takes this static from `static` dir and servers it itself.
`/assets/app.js` is Webpack entrypoint.

### README.md filling up is in progress......






