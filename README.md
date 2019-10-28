**Quick Setup**
- Setup Vagrant and pull up a vagrant terminal with root privilege as instrtucted in https://github.com/joanmarcriera/vagrant-file and run the following commands to setup
- `git clone git clone https://github.com/Frank-en-stein/EnsemblGeneSearch.git`
- `cd EnsemblGeneSearch/`
- `docker build -t emsembl-gene-search-alpine .`

**Run**
- `docker run --name emsembl-gene-search-alpine -d -p 80:5000 emsembl-gene-search-alpine`
- View OpenAPI documentation hitting the link http://localhost:8080/swagger/ from a browser on the host

**Run Tests**
- `docker exec -it emsembl-gene-search-alpine pytest`