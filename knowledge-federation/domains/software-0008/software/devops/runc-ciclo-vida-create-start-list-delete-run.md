---
id: software.devops.tranche07.000683
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

# OpenContainer runc: operações de ciclo de vida OCI (create, start, list, delete) versus comando composto run

## Em uma frase
O `runc` suporta duas formas de execução sobre um OCI bundle: o comando de conveniência `runc run` (que cria, inicia e remove o container ao sair) e as operações granulares de ciclo de vida da especificação OCI (`runc create`, `runc start`, `runc list` e `runc delete`).

## Por que importa
Se um container fosse criado e iniciado em um único passo indivisível, motores como `containerd` e plugins CNI do Kubernetes não teriam como configurar a interface de rede virtual (`veth`), atribuir o endereço IP e aplicar regras de firewall dentro do network namespace do container **antes** que o processo principal da aplicação comece a rodar. O README oficial do `runc` (`Running Containers`) explica como a separação entre `create` e `start` viabiliza essa orquestração.

## Como funciona
(1) No modo de conveniência, `runc run mycontainerid` executa em sequência a criação do ambiente, o início do processo e a remoção do container após o encerramento. (2) No modo de ciclo de vida OCI (com `"terminal": false` no `config.json`), `runc create mycontainerid` cria todos os namespaces Linux, cgroups e mounts do container e inicializa o processo auxiliar aguardando em estado `"created"` (visível em `runc list`). Nesse intervalo entre `create` e `start`, o orquestrador de nível superior configura a pilha de rede e anexos externos do container. Em seguida, `runc start mycontainerid` dispara a execução do binário configurado em `process.args`; quando o processo termina, o estado passa para `"stopped"` em `runc list`, e `runc delete mycontainerid` limpa o estado e os cgroups remanescentes.

## Exemplo
```bash
# Executar o ciclo de vida OCI completo passo a passo (create -> list -> start -> list -> delete)
cd /tmp/mycontainer
jq '.process.terminal = false | .process.args = ["sleep", "5"]' config.json > config.tmp && mv config.tmp config.json

sudo runc create mycontainerid
sudo runc list
sudo runc start mycontainerid
sleep 6
sudo runc list
sudo runc delete mycontainerid
```

## Limites e trade-offs
Ao utilizar `runc create` e `runc start` com `"terminal": false` sem configurar um socket de console ou redirecionamento explícito de descritores de arquivo, o container é lançado em segundo plano; além disso, se o processo terminar e `runc delete <id>` não for chamado, o identificador do container permanece registrado no diretório de estado em status `stopped`, impedindo a criação de outro container com o mesmo ID.

## Como verificar
Execute `sudo runc create test-lc` seguido de `sudo runc list` e confirme que a coluna `STATUS` exibe exatamente `created` antes de invocar `sudo runc start test-lc` e `sudo runc delete test-lc`.

## Conexões
- [[runc-oci-bundle-rootfs-config-json-runc-spec]] — Veja também: OpenContainer runc: criação de OCI Bundles com rootfs e geração de config.json via runc spec.
- [[runc-containers-rootless-user-namespaces-configuracao]] — Veja também: OpenContainer runc: execução de containers rootless com User Namespaces (CONFIG_USER_NS).
- [[runc-runtime-oci-referencia-linux-especificacao]] — Referência cruzada direta com runc-runtime-oci-referencia-linux-especificacao.
- [[runc-supervisores-systemd-cgroup-v2-checkpoint-criu]] — Referência cruzada direta com runc-supervisores-systemd-cgroup-v2-checkpoint-criu.

## Fontes
- [OpenContainer runc GitHub — README.md (OCI Bundles, Lifecycle, Rootless, libpathrs & Build Tags)](https://raw.githubusercontent.com/opencontainers/runc/main/README.md) — README oficial do runc detalhando criação de OCI bundles, comando runc spec, operações create/start/list/delete, containers rootless, libpathrs/seccomp e integração com systemd; consultado em 2026-10-03.
- [Open Container Initiative — Runtime Specification (runtime-spec)](https://github.com/opencontainers/runtime-spec) — Especificação oficial OCI Runtime implementada pelo runc para configuração de containers em config.json; consultado em 2026-10-03.
- [OpenContainer runc — Official GitHub Repository](https://github.com/opencontainers/runc) — Repositório oficial Apache-2.0 do runc na Open Container Initiative; consultado em 2026-10-03.
