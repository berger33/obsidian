---
id: software.devops.tranche07.000682
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/opencontainers/runc/main/README.md", "https://github.com/opencontainers/runtime-spec", "https://github.com/opencontainers/runc"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenContainer runc: criação de OCI Bundles com rootfs e geração de config.json via runc spec

## Em uma frase
Para executar um container com o `runc`, o operador prepara um OCI bundle contendo o diretório `rootfs` e gera o template de configuração `config.json` por meio do comando `runc spec`.

## Por que importa
Quando um nó Kubernetes falha ao iniciar um container com um erro críptico de `OCI runtime create failed`, engenheiros de plataforma precisam saber inspecionar ou reproduzir isoladamente o OCI bundle (`config.json` + `rootfs`) que o `containerd` ou `CRI-O` entregou ao `runc`. De acordo com o README oficial do `runc` (`Creating an OCI Bundle`), um bundle pode ser construído em segundos exportando um filesystem existente e rodando `runc spec`.

## Como funciona
Um OCI bundle consiste em um diretório pai (por exemplo, `/mycontainer`) contendo uma pasta `rootfs` populada com a árvore de arquivos do container (que pode ser obtida com `docker export $(docker create busybox) | tar -C rootfs -xvf -`) e o arquivo `config.json`. O comando `runc spec` gera um arquivo `config.json` base em conformidade com a especificação `opencontainers/runtime-spec`, definindo no bloco `process` o terminal (`"terminal": true` ou `false`), o usuário (`uid`/`gid`), os argumentos (`"args": ["sh"]`), variáveis de ambiente (`PATH`, `TERM`), conjuntos de capabilities Linux (`bounding`, `effective`, `inheritable`, `permitted`, `ambient`, como `CAP_AUDIT_WRITE`, `CAP_KILL`, `CAP_NET_BIND_SERVICE`), limites `rlimits` (`RLIMIT_NOFILE`) e `"noNewPrivileges": true`.

## Exemplo
```bash
# Criar um OCI bundle completo a partir do busybox e gerar o arquivo config.json padrão com runc spec
mkdir -p /tmp/mycontainer/rootfs
cd /tmp/mycontainer
docker export $(docker create busybox) | tar -C rootfs -xvf -
runc spec
ls -la config.json rootfs/
```

## Limites e trade-offs
O template padrão gerado por `runc spec` vem com `"terminal": true` (esperando uma sessão interativa de TTY) e com o filesystem raiz configurado como somente leitura (`"readonly": true`) no bloco `root`; para rodar o container em segundo plano ou permitir escritas no `rootfs`, é obrigatório editar o `config.json` ajustando `"terminal": false` e `"readonly": false`.

## Como verificar
Após executar `runc spec`, valide a estrutura do JSON gerado com `jq .process config.json` e confirme que os campos `args`, `capabilities`, `rlimits` e `noNewPrivileges` estão presentes.

## Conexões
- [[runc-runtime-oci-referencia-linux-especificacao]] — Veja também: OpenContainer runc: ferramenta CLI e runtime de referência para criar e executar containers segundo a especificação OCI.
- [[runc-ciclo-vida-create-start-list-delete-run]] — Veja também: OpenContainer runc: operações de ciclo de vida OCI (create, start, list, delete) versus comando composto run.
- [[runc-containers-rootless-user-namespaces-configuracao]] — Referência cruzada direta com runc-containers-rootless-user-namespaces-configuracao.

## Fontes
- [OpenContainer runc GitHub — README.md (OCI Bundles, Lifecycle, Rootless, libpathrs & Build Tags)](https://raw.githubusercontent.com/opencontainers/runc/main/README.md) — README oficial do runc detalhando criação de OCI bundles, comando runc spec, operações create/start/list/delete, containers rootless, libpathrs/seccomp e integração com systemd; consultado em 2026-10-03.
- [Open Container Initiative — Runtime Specification (runtime-spec)](https://github.com/opencontainers/runtime-spec) — Especificação oficial OCI Runtime implementada pelo runc para configuração de containers em config.json; consultado em 2026-10-03.
- [OpenContainer runc — Official GitHub Repository](https://github.com/opencontainers/runc) — Repositório oficial Apache-2.0 do runc na Open Container Initiative; consultado em 2026-10-03.
