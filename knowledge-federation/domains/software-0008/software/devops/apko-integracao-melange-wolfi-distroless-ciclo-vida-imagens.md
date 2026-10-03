---
id: software.devops.tranche14.001370
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
fontes: ["https://raw.githubusercontent.com/chainguard-dev/apko/main/README.md", "https://raw.githubusercontent.com/chainguard-dev/apko/main/docs/apko_file.md", "https://github.com/chainguard-dev/apko"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# apko: Arquitetura Combinada melange + apko para Imagens Distroless Zero-CVE com Wolfi

## Em uma frase
A combinação do **melange** (que compila código-fonte em pacotes `.apk` assinados) com o **apko** (que monta pacotes `.apk` em imagens OCI distroless com SBOM) forma a base da fábrica de software segura usada no ecossistema **Wolfi** e Chainguard Images.

## Por que importa
Imagens baseadas em distribuições completas carregam gerenciadores de pacotes, shells e dezenas de binários não utilizados que acumulam CVEs e ampliam a superfície de ataque pós-exploração.

## Como funciona
No pipeline unificado, o `melange` compila a aplicação e gera os subpacotes (separando binário de runtime, headers `-dev` e documentação `-doc`), e o `apko` instala na imagem de produção apenas o pacote de runtime e suas bibliotecas compartilhadas estritas (`glibc`/`libstdc++`), resultando em uma imagem mínima, sem shell e com SBOM completo.

## Exemplo
```bash
docker run --rm -v "$PWD":/work cgr.dev/chainguard/apko build \
  /work/apko.yaml app-distroless:v1 /work/app-distroless.tar
```

## Limites e trade-offs
Tentar usar o `apko` sozinho quando o projeto ainda exige executar scripts complexos de instalação não empacotados em `.apk` gera bloqueio; nesses casos, a própria documentação recomenda gerar a imagem base segura com `apko` e usar um `Dockerfile` mínimo apenas para o passo final.

## Como verificar
Priorize empacotar a aplicação com `melange` para obter imagens 100% declarativas no `apko`, ou use a imagem gerada pelo `apko` como estágio `FROM` final.

## Conexões
- [[apko-lockfile-apko-lock-json-pinning-exato-versoes-digests]] — Veja também: apko: Pinagem Determinística de Pacotes e Digests com apko lock (apko.lock.json).

## Fontes
- [apko GitHub — README.md (APK-Based Reproducible OCI Image Builder, apko build, apko publish, SBOM Generation & Declarative Design)](https://raw.githubusercontent.com/chainguard-dev/apko/main/README.md) — README oficial do chainguard-dev/apko detalhando reprodutibilidade bitwise sem instruções RUN, geração automática de SBOM, integração com melange e supervisão s6; consultado em 2026-10-03.
- [apko Official Documentation — docs/apko_file.md (contents, repositories, runtime_keyring, entrypoint, accounts, paths, archs & layering)](https://raw.githubusercontent.com/chainguard-dev/apko/main/docs/apko_file.md) — Referência completa do formato YAML do apko cobrindo repositórios @local, runtime_repositories/runtime_keyring, accounts non-root, mutações de paths e layering.strategy; consultado em 2026-10-03.
- [Chainguard apko — Official GitHub Repository](https://github.com/chainguard-dev/apko) — Repositório oficial Apache-2.0 do apko; consultado em 2026-10-03.
