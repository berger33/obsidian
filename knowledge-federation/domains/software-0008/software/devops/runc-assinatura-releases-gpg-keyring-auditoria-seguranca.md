---
id: software.devops.tranche07.000689
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

# OpenContainer runc: verificação de releases assinadas com runc.keyring, auditoria Cure53 e processo de segurança OCI

## Em uma frase
Todas as releases oficiais do `runc` são assinadas criptograficamente por chaves PGP listadas no arquivo `runc.keyring` na raiz do repositório, seguindo o processo de divulgação de segurança da OCI e contando com auditoria independente da Cure53.

## Por que importa
Por ser o binário executado com privilégios máximos no host Linux toda vez que um container inicia no Docker ou no Kubernetes, comprometer o binário do `runc` na cadeia de suprimentos (supply chain) daria acesso root a milhões de servidores. Segundo as seções `Releases` e `Security` do README oficial do `runc`, verificar a assinatura das releases contra o `runc.keyring` garante a autenticidade e integridade dos artefatos baixados.

## Como funciona
Na raiz do repositório `opencontainers/runc`, o arquivo `runc.keyring` armazena o conjunto oficial de chaves públicas OpenPGP dos mantenedores autorizados a assinar releases. A cada nova versão publicada na página de Releases do GitHub, os binários (`runc.amd64`, `runc.arm64`, etc.), o tarball de código-fonte e o arquivo `runc.sha256sum` são acompanhados de assinaturas destacáveis `.asc`. Além disso, o projeto segue a política formal de comunicação e embargo de vulnerabilidades da Open Container Initiative (`SECURITY.md`) e disponibiliza publicamente em `docs/Security-Audit.pdf` o relatório completo da auditoria de segurança de terceiros conduzida pela Cure53.

## Exemplo
```bash
# Importar o keyring oficial do runc e verificar a assinatura GPG de uma release baixada
gpg --no-default-keyring --keyring ./runc-trusted.gpg --import runc.keyring
gpg --no-default-keyring --keyring ./runc-trusted.gpg --verify runc.amd64.asc runc.amd64
sha256sum -c runc.sha256sum --ignore-missing
```

## Limites e trade-offs
Baixar o binário `runc.amd64` em scripts de provisionamento de nós Kubernetes (como imagens de AMI/Packer) verificando apenas o checksum SHA-256 sem validar a assinatura GPG contra o `runc.keyring` protege contra corrupção de rede, mas não garante autenticidade criptográfica do mantenedor caso o espelho de download seja comprometido.

## Como verificar
Execute `gpg --show-keys runc.keyring` na raiz do repositório do `runc` para listar as impressões digitais (fingerprints) das chaves dos mantenedores autorizados.

## Conexões
- [[runc-testes-integracao-bats-rootless-go-modules]] — Veja também: OpenContainer runc: suíte de testes isolada em container (make test, BATS, rootless) e gestão de dependências Go.
- [[runc-gerenciamento-terminais-tty-console-socket-stdio]] — Veja também: OpenContainer runc: gerenciamento de terminais pseudo-TTY (--console-socket), descritores stdio e capabilities.
- [[runc-runtime-oci-referencia-linux-especificacao]] — Referência cruzada direta com runc-runtime-oci-referencia-linux-especificacao.
- [[runc-seguranca-path-safety-libpathrs-seccomp]] — Referência cruzada direta com runc-seguranca-path-safety-libpathrs-seccomp.
- [[crun-runtime-oci-linguagem-c-baixo-consumo-memoria]] — Referência cruzada direta com crun-runtime-oci-linguagem-c-baixo-consumo-memoria.

## Fontes
- [OpenContainer runc GitHub — README.md (OCI Bundles, Lifecycle, Rootless, libpathrs & Build Tags)](https://raw.githubusercontent.com/opencontainers/runc/main/README.md) — README oficial do runc detalhando criação de OCI bundles, comando runc spec, operações create/start/list/delete, containers rootless, libpathrs/seccomp e integração com systemd; consultado em 2026-10-03.
- [Open Container Initiative — Runtime Specification (runtime-spec)](https://github.com/opencontainers/runtime-spec) — Especificação oficial OCI Runtime implementada pelo runc para configuração de containers em config.json; consultado em 2026-10-03.
- [OpenContainer runc — Official GitHub Repository](https://github.com/opencontainers/runc) — Repositório oficial Apache-2.0 do runc na Open Container Initiative; consultado em 2026-10-03.
