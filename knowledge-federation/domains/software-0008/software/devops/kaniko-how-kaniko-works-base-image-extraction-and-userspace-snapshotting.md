---
id: software.devops.tranche06.000552
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

# Como o Kaniko funciona: extração da imagem base e snapshotting do sistema de arquivos em userspace

## Em uma frase
A seção *How does kaniko work?* do README oficial explica o mecanismo interno que permite construir imagens sem privilégios de kernel (`chroot` ou `bind-mount`) e sem daemon Docker: dentro da imagem executora **`gcr.io/kaniko-project/executor`**, o Kaniko (1) **extrai o sistema de arquivos da imagem base** (a imagem especificada em `FROM` no `Dockerfile`) diretamente na raiz do próprio contêiner executor; (2) **executa os comandos do `Dockerfile` um por um**; (3) **tira um snapshot do sistema de arquivos em userspace após cada comando**; e (4) **anexa uma camada contendo os arquivos alterados** sobre a imagem base (se houver mudanças) e atualiza os metadados da imagem antes de enviá-la ao registro de destino (`--destination`).

## Por que importa
Compreender que o Kaniko descompacta a imagem base diretamente sobre a raiz `/` do seu próprio contêiner (enquanto protege seus próprios binários e credenciais em `/kaniko`) explica por que ele não exige `privileged: true` no Kubernetes, mas também por que ele não pode ser copiado para dentro de outras imagens.

## Como funciona
Sempre execute o Kaniko utilizando a imagem oficial dedicada `gcr.io/kaniko-project/executor` (ou a variante `:debug` quando precisar de um shell para integração de CI), guardando arquivos de configuração e certificados dentro do diretório protegido `/kaniko` (como `/kaniko/.docker/` e `/kaniko/ssl/certs/`).

## Exemplo
Quando um pod do Kaniko inicia o build de `FROM python:3.12-slim`, ele extrai o rootfs do Python em `/`, roda `RUN pip install -r requirements.txt`, calcula em userspace o diff dos arquivos modificados em relação ao snapshot anterior e gera a nova camada `.tar.gz`.

## Limites e trade-offs
Quando um `Dockerfile` tiver muitos arquivos mas poucos comandos que alteram diretórios específicos, avalie as flags **`--snapshot-mode`** (`full`, `redo` ou `time`), **`--single-snapshot`** e **`--use-new-run`** documentadas no README para otimizar o tempo de varredura do sistema de arquivos em userspace.

## Como verificar
Acompanhe os logs do executor Kaniko (`--verbosity=info` ou `debug`) verificando as mensagens `Unpacking rootfs`, `Taking snapshot of full filesystem...` e o push final da imagem.

## Conexões
- [[kaniko-userspace-dockerfile-builds-and-upstream-archival-status]] — Veja também: Execução de Dockerfile em userspace no Kaniko e seu status de projeto arquivado upstream.
- [[kaniko-known-issues-official-executor-image-requirement]] — Veja também: Limitações conhecidas do Kaniko: proibição de copiar o binário executor para outras imagens (como agentes Jenkins).

## Fontes
- [Kaniko GitHub — README.md (Archival Notice, Userspace Dockerfile Execution, Build Contexts, Caching & Known Issues)](https://raw.githubusercontent.com/GoogleContainerTools/kaniko/main/README.md) — README oficial do Kaniko (GoogleContainerTools/kaniko) registrando o aviso no topo de que o projeto está arquivado e não é mais mantido, seu funcionamento por extração do rootfs e snapshotting em userspace sem daemon Docker dentro de gcr.io/kaniko-project/executor, os 7 contextos de build suportados, cache de camadas (--cache, --cache-repo) e cache de imagens base (gcr.io/kaniko-project/warmer), execução em Kubernetes/gVisor e limitações conhecidas.; consultado em 2026-10-03.
- [Kaniko GitHub — Getting Started Tutorial (docs/tutorial.md)](https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md) — Tutorial histórico oficial de uso do Kaniko em clusters Kubernetes.; consultado em 2026-10-03.
- [Kaniko — Official GitHub Repository (Archived)](https://github.com/GoogleContainerTools/kaniko) — Repositório oficial Apache-2.0 arquivado do Kaniko em GoogleContainerTools.; consultado em 2026-10-03.
