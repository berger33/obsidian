---
id: software.devops.tranche14.001369
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

# apko: Pinagem Determinística de Pacotes e Digests com apko lock (apko.lock.json)

## Em uma frase
O comando `apko lock <config.yaml>` resolve todas as versões transitivas de pacotes APK e seus digests criptográficos no momento da execução e grava um arquivo de trava (`apko.lock.json`), garantindo que builds futuros usem exatamente os mesmos binários.

## Por que importa
Mesmo que o `apko` seja bitwise reproducible para o mesmo conjunto de pacotes de entrada, os repositórios Alpine ou Wolfi publicam novas versões de pacotes continuamente; sem um lockfile, rodar `apko build` na semana seguinte puxará versões mais novas dos pacotes.

## Como funciona
Com o arquivo `.lock.json` versionado no Git, o pipeline de CI executa `apko build --lockfile apko.lock.json`, reproduzindo exatamente o mesmo digest de imagem OCI em qualquer lugar ou época, enquanto um job automatizado roda `apko lock` para propor atualizações via Pull Request.

## Exemplo
```bash
apko lock apko.yaml
apko build --lockfile apko.lock.json apko.yaml my-app:v1.0.0 my-app.tar
```

## Limites e trade-offs
Atualizar a lista `contents.packages` no `apko.yaml` e rodar `apko build --lockfile apko.lock.json` sem regerar o lockfile com `apko lock` falha porque o lockfile não contém a resolução do novo pacote.

## Como verificar
Sempre que adicionar ou remover pacotes em `apko.yaml`, execute `apko lock apko.yaml` e inclua o `apko.lock.json` atualizado no mesmo commit.

## Conexões
- [[apko-layering-strategy-origin-budget-otimizacao-cache-camadas]] — Veja também: apko: Estratégia de Divisão em Camadas (layering.strategy e budget) para Eficiência de Pull.
- [[apko-integracao-melange-wolfi-distroless-ciclo-vida-imagens]] — Veja também: apko: Arquitetura Combinada melange + apko para Imagens Distroless Zero-CVE com Wolfi.

## Fontes
- [apko GitHub — README.md (APK-Based Reproducible OCI Image Builder, apko build, apko publish, SBOM Generation & Declarative Design)](https://raw.githubusercontent.com/chainguard-dev/apko/main/README.md) — README oficial do chainguard-dev/apko detalhando reprodutibilidade bitwise sem instruções RUN, geração automática de SBOM, integração com melange e supervisão s6; consultado em 2026-10-03.
- [apko Official Documentation — docs/apko_file.md (contents, repositories, runtime_keyring, entrypoint, accounts, paths, archs & layering)](https://raw.githubusercontent.com/chainguard-dev/apko/main/docs/apko_file.md) — Referência completa do formato YAML do apko cobrindo repositórios @local, runtime_repositories/runtime_keyring, accounts non-root, mutações de paths e layering.strategy; consultado em 2026-10-03.
- [Chainguard apko — Official GitHub Repository](https://github.com/chainguard-dev/apko) — Repositório oficial Apache-2.0 do apko; consultado em 2026-10-03.
