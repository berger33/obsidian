---
id: software.devops.tranche09.000863
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/ko-build/ko/main/README.md", "https://ko.build/get-started/", "https://ko.build/features/k8s/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# ko: integração nativa com manifestos Kubernetes via referências ko://, ko resolve, ko apply e ko delete

## Em uma frase
O `ko` permite referenciar pacotes Go diretamente no campo `image:` de manifestos Kubernetes usando o prefixo `ko://<importpath>`, onde `ko resolve -f` compila, publica e substitui a URI pelo digest SHA-256 exato da imagem construída, e `ko apply -f` aplica tudo ao cluster em um único passo.

## Por que importa
No desenvolvimento tradicional para Kubernetes, alterar uma linha de código Go exige rodar `docker build`, criar uma tag, fazer `docker push`, copiar o digest SHA-256 gerado, editar o arquivo `deployment.yaml` com o novo digest e rodar `kubectl apply`. Conforme explica a página oficial `Kubernetes Integration` (`ko.build/features/k8s/`), o `ko` transforma o empacotamento e o push de imagens em um detalhe de implementação invisível.

## Como funciona
No manifesto YAML do Kubernetes (`Deployment`, `Job`, `StatefulSet`, `CronJob`), em vez de escrever uma tag de imagem tradicional, o desenvolvedor escreve **`image: ko://github.com/meu-org/meu-repo/cmd/app`**. Ao executar **`ko resolve -f config/ > release.yaml`**, o `ko`: (1) varre todos os arquivos YAML em busca de strings com o prefixo `ko://`; (2) para cada importpath único encontrado, executa `ko build <importpath>` em paralelo (compilando e enviando a imagem para `KO_DOCKER_REPO`); (3) substitui a string `ko://...` no YAML pela referência completa com digest imutável (`registry.../app@sha256:...`); e (4) imprime o YAML resolvido no `stdout`. Para aplicar diretamente ao cluster sem arquivo intermediário, usa-se **`ko apply -f config/`** (e **`ko delete -f config/`** como atalho para `kubectl delete`).

## Exemplo
```bash
# Resolver todas as referências ko:// em config/ gerando release.yaml ou aplicar diretamente ao cluster Kubernetes
ko resolve -f config/ > release.yaml
ko apply -f config/ -- --context=staging-cluster
```

## Limites e trade-offs
O comando `ko apply -f config/` exige que o binário `kubectl` esteja instalado e disponível no `$PATH` da máquina (repassando quaisquer flags após `--` diretamente para o `kubectl apply`); já o comando `ko resolve -f config/` não depende de `kubectl` nem de acesso ao cluster Kubernetes, sendo ideal para o estágio de build do CI que gera o artefato `release.yaml` imutável.

## Como verificar
Execute `ko resolve -f deployment.yaml` com `KO_DOCKER_REPO=ko.local` e verifique no YAML impresso no `stdout` que o campo `image: ko://...` foi substituído por `ko.local/...:...@sha256:...`.

## Conexões
- [[ko-autenticacao-registries-ko-docker-repo-ko-login]] — Veja também: ko: autenticação transparente em registries (GCR/GAR, ECR, ACR, GHCR e ko login) e variável KO_DOCKER_REPO.
- [[ko-geracao-automatica-sbom-multiplataforma-reprodutibilidade]] — Veja também: ko: builds multiplataforma (--platform=all), geração de SBOM por padrão e reprodutibilidade.
- [[ko-construtor-imagens-containers-go-sem-docker]] — Referência cruzada direta com ko-construtor-imagens-containers-go-sem-docker.
- [[ko-desenvolvimento-local-ko-local-kind-local-minikube]] — Referência cruzada direta com ko-desenvolvimento-local-ko-local-kind-local-minikube.
- [[kind-carregamento-imagens-locais-load-docker-image-archive]] — Referência cruzada direta com kind-carregamento-imagens-locais-load-docker-image-archive.

## Fontes
- [ko GitHub — README.md (Fast Go Container Builder, Multi-Platform, Automatic SBOMs & Bazel Heritage)](https://raw.githubusercontent.com/ko-build/ko/main/README.md) — README oficial do ko-build/ko (CNCF Sandbox) cobrindo compilação local Go sem Docker, suporte multiplataforma, geração de SBOM por padrão e integração com YAML do Kubernetes; consultado em 2026-10-03.
- [ko Official Documentation — Get Started (Authentication, KO_DOCKER_REPO, Naming Strategies & Local Publishing)](https://ko.build/get-started/) — Guia oficial Get Started do ko detalhando autenticação nativa (GCR/GAR, ECR, ACR, GHCR e ko login), KO_DOCKER_REPO, entrypoint /ko-app/<app>, estratégias de nomes (-B, -P, --bare) e destinos locais ko.local e kind.local; consultado em 2026-10-03.
- [ko Official Documentation — Kubernetes Integration (ko:// Importpaths, ko resolve, ko apply & ko delete)](https://ko.build/features/k8s/) — Documentação oficial de integração do ko com manifestos Kubernetes usando referências ko://, ko resolve, ko apply e ko delete; consultado em 2026-10-03.
