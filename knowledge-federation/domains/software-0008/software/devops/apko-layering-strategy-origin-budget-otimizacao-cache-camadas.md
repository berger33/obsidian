---
id: software.devops.tranche14.001368
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
fontes: ["https://raw.githubusercontent.com/chainguard-dev/apko/main/docs/apko_file.md", "https://raw.githubusercontent.com/chainguard-dev/apko/main/README.md", "https://github.com/chainguard-dev/apko"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# apko: Estratégia de Divisão em Camadas (layering.strategy e budget) para Eficiência de Pull

## Em uma frase
Por padrão, o `apko` pode empacotar todo o sistema de arquivos em uma única camada OCI enxuta ou dividir os pacotes inteligentemente em múltiplas camadas usando a seção `layering` (`strategy: origin` e `budget: <N>`).

## Por que importa
Se uma imagem contém `glibc`, `openssl`, `python3` e um pequeno pacote da aplicação em uma única camada monolítica, atualizar apenas o pacote da aplicação obriga os nós Kubernetes a baixarem novamente toda a camada com Python e bibliotecas base.

## Como funciona
Configurando `layering.strategy: origin` com um orçamento máximo de camadas (`budget: 10`), o `apko` agrupa pacotes relacionados em camadas separadas deterministicamente sem ultrapassar o limite definido por `budget`, maximizando o reuso de cache de blobs no `containerd`.

## Exemplo
```yaml
layering:
  strategy: origin
  budget: 10
```

## Limites e trade-offs
Definir um `budget` de camadas muito alto (dezenas de camadas minúsculas) aumenta a sobrecarga de metadados de manifesto e de montagem de diretórios no snapshotter `overlayfs`.

## Como verificar
Utilize um `budget` moderado (entre `4` e `10` camadas) com `strategy: origin` para equilibrar reuso de cache e simplicidade de manifesto.

## Conexões
- [[apko-multi-arch-archs-publish-oci-image-index-sbom]] — Veja também: apko: Construção e Publicação Multi-Arquitetura (archs e apko publish) com Geração Automática de SBOM.
- [[apko-lockfile-apko-lock-json-pinning-exato-versoes-digests]] — Veja também: apko: Pinagem Determinística de Pacotes e Digests com apko lock (apko.lock.json).

## Fontes
- [apko GitHub — README.md (APK-Based Reproducible OCI Image Builder, apko build, apko publish, SBOM Generation & Declarative Design)](https://raw.githubusercontent.com/chainguard-dev/apko/main/docs/apko_file.md) — README oficial do chainguard-dev/apko detalhando reprodutibilidade bitwise sem instruções RUN, geração automática de SBOM, integração com melange e supervisão s6; consultado em 2026-10-03.
- [apko Official Documentation — docs/apko_file.md (contents, repositories, runtime_keyring, entrypoint, accounts, paths, archs & layering)](https://raw.githubusercontent.com/chainguard-dev/apko/main/README.md) — Referência completa do formato YAML do apko cobrindo repositórios @local, runtime_repositories/runtime_keyring, accounts non-root, mutações de paths e layering.strategy; consultado em 2026-10-03.
- [Chainguard apko — Official GitHub Repository](https://github.com/chainguard-dev/apko) — Repositório oficial Apache-2.0 do apko; consultado em 2026-10-03.
