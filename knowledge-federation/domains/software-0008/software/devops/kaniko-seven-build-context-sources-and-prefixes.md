---
id: software.devops.tranche06.000554
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/GoogleContainerTools/kaniko/main/README.md", "https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md", "https://github.com/GoogleContainerTools/kaniko"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Os sete contextos de build suportados pelo Kaniko (dir, tar, stdin, gs, s3, https Azure e git)

## Em uma frase
A seção *kaniko Build Contexts* do README oficial documenta as **sete fontes e prefixos de URI** aceitos pela flag **`--context`** para buscar o diretório contendo o `Dockerfile` e os arquivos do projeto: (1) **Diretório local** montado dentro do contêiner: `dir:///workspace` (padrão caso nenhum prefixo seja informado); (2) **Arquivo `.tar.gz` local** montado no contêiner: `tar:///path/to/context.tar.gz`; (3) **Entrada padrão (`STDIN`)** em formato `.tar.gz`: `tar://stdin` (exigindo `-i`/`--interactive` / `stdin: true`); (4) **Google Cloud Storage (GCS)**: `gs://kaniko-bucket/path/to/context.tar.gz`; (5) **Amazon S3**: `s3://kaniko-bucket/path/to/context.tar.gz`; (6) **Azure Blob Storage**: `https://myaccount.blob.core.windows.net/container/path/to/context.tar.gz` (autenticado via variável de ambiente `AZURE_STORAGE_ACCESS_KEY`); e (7) **Repositório Git** direto: `git://github.com/acme/myproject.git#refs/heads/mybranch#<desired-commit-id>` (autenticado para repositórios privados via `GIT_TOKEN` ou `GIT_USERNAME`/`GIT_PASSWORD`).

## Por que importa
Suportar buckets de nuvem (`gs://`, `s3://`, Azure Blob), `git://` e `tar://stdin` diretamente no `--context` permite executar um Pod avulso do Kaniko em qualquer cluster Kubernetes sem precisar sequer provisionar um PersistentVolume ou contêiner de init para baixar o código-fonte.

## Como funciona
Escolha o prefixo `--context` mais adequado à sua arquitetura de CI: use `dir:///workspace` quando um step anterior no mesmo Pod já baixou o código, `git://...` com `GIT_TOKEN` para builds autônomos diretos do Git ou `tar://stdin` para enviar contextos efêmeros sem armazenamento intermediário.

## Exemplo
Um serviço de plataforma dispara um Job Kubernetes com um único contêiner Kaniko passando `--context=git://github.com/empresa/api.git#refs/heads/main#a1b2c3d` e a variável `GIT_TOKEN` vinda de um Secret, construindo e publicando a imagem sem precisar de volumes persistentes.

## Limites e trade-offs
Ao usar buckets `gs://` ou `s3://` ou `tar://stdin`, lembre-se da exigência documentada no README: o contexto deve ser empacotado previamente como um arquivo tar comprimido com gzip (**`.tar.gz`**, por exemplo `tar -C <path> -zcvf context.tar.gz .`).

## Como verificar
Verifique nos logs iniciais do Kaniko a mensagem de resolução e extração bem-sucedida do `--context` configurado antes do início da primeira instrução do `Dockerfile`.

## Conexões
- [[kaniko-known-issues-official-executor-image-requirement]] — Veja também: Limitações conhecidas do Kaniko: proibição de copiar o binário executor para outras imagens (como agentes Jenkins).
- [[kaniko-remote-layer-caching-and-base-image-warmer]] — Veja também: Cache remoto de camadas (--cache, --cache-repo) e pré-aquecimento local de imagens base (kaniko warmer).

## Fontes
- [Kaniko GitHub — README.md (Archival Notice, Userspace Dockerfile Execution, Build Contexts, Caching & Known Issues)](https://raw.githubusercontent.com/GoogleContainerTools/kaniko/main/README.md) — README oficial do Kaniko (GoogleContainerTools/kaniko) registrando o aviso no topo de que o projeto está arquivado e não é mais mantido, seu funcionamento por extração do rootfs e snapshotting em userspace sem daemon Docker dentro de gcr.io/kaniko-project/executor, os 7 contextos de build suportados, cache de camadas (--cache, --cache-repo) e cache de imagens base (gcr.io/kaniko-project/warmer), execução em Kubernetes/gVisor e limitações conhecidas.; consultado em 2026-10-03.
- [Kaniko GitHub — Getting Started Tutorial (docs/tutorial.md)](https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md) — Tutorial histórico oficial de uso do Kaniko em clusters Kubernetes.; consultado em 2026-10-03.
- [Kaniko — Official GitHub Repository (Archived)](https://github.com/GoogleContainerTools/kaniko) — Repositório oficial Apache-2.0 arquivado do Kaniko em GoogleContainerTools.; consultado em 2026-10-03.
