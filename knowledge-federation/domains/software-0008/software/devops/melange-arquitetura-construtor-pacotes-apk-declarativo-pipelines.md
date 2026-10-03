---
id: software.devops.tranche14.001371
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/chainguard-dev/melange/main/README.md", "https://raw.githubusercontent.com/chainguard-dev/melange/main/docs/BUILD-FILE.md", "https://github.com/chainguard-dev/melange"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# melange: Construtor Declarativo de Pacotes APK Baseado em Pipelines para Imagens de Container

## Em uma frase
O **melange** (`chainguard-dev/melange`) é o compilador declarativo de pacotes **APK** criado pela Chainguard para construir artefatos de software auditáveis (para os ecossistemas **Wolfi** e **Alpine Linux**) que alimentam diretamente o construtor de imagens OCI **apko**.

## Por que importa
Gerenciadores de pacotes tradicionais (`APKBUILD`, `RPM spec` ou `debian/rules`) utilizam scripts rígidos divididos em fases fixas e difíceis de compor ou auditar em fábricas de software modernas.

## Como funciona
No `melange`, todo o processo de compilação é declarado em um arquivo YAML (`melange.yaml`) estruturado em três seções obrigatórias: **`package`** (metadados, versão, época, licenças e dependências de runtime), **`environment`** (configuração estilo `apko` do ambiente de build efêmero) e **`pipeline`** (lista ordenada e componível de passos de compilação).

## Exemplo
```bash
melange version
melange keygen
melange build examples/gnu-hello.yaml --arch $(uname -m) --signing-key melange.rsa
```

## Limites e trade-offs
Executar `melange build` dentro de um container Docker sem a flag `--privileged` (ou sem suporte a bubblewrap/namespaces de isolamento requerido pelo runner do melange) falha ao montar o ambiente isolado de compilação.

## Como verificar
Ao rodar o container oficial `cgr.dev/chainguard/melange`, passe `--privileged` e monte o diretório de trabalho com `-v "$PWD":/work`.

## Conexões
- [[melange-package-metadata-version-epoch-copyright-spdx]] — Veja também: melange: Metadados de Pacote (name, version, epoch) e Atestação de Licenças SPDX (copyright).

## Fontes
- [melange GitHub — README.md (Declarative APK Package Builder, Pipeline Builds, QEMU Multi-Arch, melange keygen, Default Substitutions & Debugging)](https://raw.githubusercontent.com/chainguard-dev/melange/main/README.md) — README oficial do chainguard-dev/melange documentando o arquivo de build, variáveis de substituição (${{package.*}}, ${{targets.destdir}}), assinatura RSA, subpackages e uso conjunto com apko; consultado em 2026-10-03.
- [melange Official Documentation — docs/BUILD-FILE.md (package, version, epoch, copyright SPDX, dependencies.provides, options & environment)](https://raw.githubusercontent.com/chainguard-dev/melange/main/docs/BUILD-FILE.md) — Especificação oficial do arquivo de build do melange detalhando version/epoch, licenças SPDX em copyright, fluxos de versão com provides e controles do gerador SCA em options; consultado em 2026-10-03.
- [Chainguard melange — Official GitHub Repository](https://github.com/chainguard-dev/melange) — Repositório oficial Apache-2.0 do melange; consultado em 2026-10-03.
