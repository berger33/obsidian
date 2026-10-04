---
id: software.devops.tranche07.000688
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

# OpenContainer runc: suíte de testes isolada em container (make test, BATS, rootless) e gestão de dependências Go

## Em uma frase
O repositório do `runc` executa sua suíte de testes unitários e de integração (BATS e rootless) dentro de containers via `make test` (`TESTFLAGS`, `TESTPATH`, `ROOTLESS_TESTPATH`) e gerencia dependências Go com vendoring (`make vendor` e `make verify-dependencies`).

## Por que importa
Como os testes de um runtime de containers manipulam mounts, namespaces, cgroups, dispositivos e arquivos em todo o sistema operacional, executá-los diretamente na máquina de desenvolvimento sem isolamento pode modificar ou remover arquivos do host. Conforme alerta a seção `Running the test suite` do README oficial do `runc`, a execução dos testes fora de um container não é recomendada, pois os testes assumem que podem escrever e remover arquivos em qualquer lugar.

## Como funciona
O comando `make test` constrói uma imagem de container de teste contendo todas as dependências (incluindo `libpathrs`, `libseccomp`, `criu` e `bats`) e executa a suíte de forma isolada. O desenvolvedor pode filtrar um caso de teste unitário específico em Go definindo `TESTFLAGS="-run=SomeTestFunction"`, rodar apenas um arquivo de teste de integração BATS com `TESTPATH="/checkpoint.bats"` ou executar um teste de integração rootless específico com `ROOTLESS_TESTPATH="/checkpoint.bats"`, além de passar flags de proxy/engine via `CONTAINER_ENGINE_BUILD_FLAGS` e `CONTAINER_ENGINE_RUN_FLAGS`. Para gerenciamento de módulos Go, o projeto mantém dependências vendored no repositório, atualizadas via `make vendor` e auditadas no CI com `make verify-dependencies`.

## Exemplo
```bash
# Executar um teste de integração BATS específico e verificar dependências vendored no repositório do runc
make test TESTPATH="/checkpoint.bats"
make verify-dependencies
```

## Limites e trade-offs
Embora existam alvos no Makefile (`localunittest`, `localintegration`) para rodar testes diretamente no host Linux (usados dentro de máquinas virtuais efêmeras de CI), rodá-los em uma estação de trabalho compartilhada pode deixar mounts órfãos, cgroups de teste ou alterações no sistema de arquivos local.

## Como verificar
Em um clone do repositório `opencontainers/runc`, execute `make verify-dependencies` para confirmar que o diretório `vendor/` e o `go.mod`/`go.sum` estão íntegros e sem divergências.

## Conexões
- [[runc-supervisores-systemd-cgroup-v2-checkpoint-criu]] — Veja também: OpenContainer runc: integração com supervisores systemd, cgroup v2 e Checkpoint/Restore com CRIU.
- [[runc-assinatura-releases-gpg-keyring-auditoria-seguranca]] — Veja também: OpenContainer runc: verificação de releases assinadas com runc.keyring, auditoria Cure53 e processo de segurança OCI.
- [[runc-runtime-oci-referencia-linux-especificacao]] — Referência cruzada direta com runc-runtime-oci-referencia-linux-especificacao.
- [[runc-compilacao-build-tags-nocriu-obsoletos]] — Referência cruzada direta com runc-compilacao-build-tags-nocriu-obsoletos.

## Fontes
- [OpenContainer runc GitHub — README.md (OCI Bundles, Lifecycle, Rootless, libpathrs & Build Tags)](https://raw.githubusercontent.com/opencontainers/runc/main/README.md) — README oficial do runc detalhando criação de OCI bundles, comando runc spec, operações create/start/list/delete, containers rootless, libpathrs/seccomp e integração com systemd; consultado em 2026-10-03.
- [Open Container Initiative — Runtime Specification (runtime-spec)](https://github.com/opencontainers/runtime-spec) — Especificação oficial OCI Runtime implementada pelo runc para configuração de containers em config.json; consultado em 2026-10-03.
- [OpenContainer runc — Official GitHub Repository](https://github.com/opencontainers/runc) — Repositório oficial Apache-2.0 do runc na Open Container Initiative; consultado em 2026-10-03.
