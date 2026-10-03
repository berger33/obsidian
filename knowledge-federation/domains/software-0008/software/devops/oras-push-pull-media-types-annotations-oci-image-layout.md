---
id: software.devops.tranche13.001252
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://oras.land/docs/category/oras-commands/", "https://raw.githubusercontent.com/oras-project/oras/main/README.md", "https://github.com/oras-project/oras"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# ORAS: Operações de Push e Pull de Arquivos, Media Types, Anotações e OCI Image Layout Local

## Em uma frase
Os subcomandos `oras push` e `oras pull` transferem arquivos e diretórios entre o sistema de arquivos local, registros remotos e diretórios locais no formato **OCI Image Layout** (`--oci-layout`), preservando permissões, estrutura de pastas e anotações de manifesto.

## Por que importa
Durante o build em ambientes air-gapped ou pipelines de CI, frequentemente é necessário construir e inspecionar o pacote OCI localmente em disco (`--oci-layout`) antes de autenticá-lo e enviá-lo para o registry remoto.

## Como funciona
No comando `oras push <alvo> <arquivo>:<media-type>`, o ORAS cria os blobs para cada arquivo ou diretório (comprimindo diretórios automaticamente como tarballs), gera o manifesto OCI com as `--annotation` informadas e faz upload para o registry. No sentido inverso, `oras pull <alvo> -o ./destino` baixa apenas os blobs de artefatos e reconstrói os arquivos localmente.

## Exemplo
```bash
# Empurrar para um diretorio local em formato OCI Image Layout e depois baixar:
oras push --oci-layout ./local-oci-store:v1 \
  --annotation "org.opencontainers.image.description=Config bundle" \
  config.yaml:application/yaml
oras pull --oci-layout ./local-oci-store:v1 -o ./restored-config
```

## Limites e trade-offs
Usar caminhos absolutos ou referências `../` fora do diretório de trabalho ao fazer `oras push` sem normalizar os caminhos pode causar rejeição de extração por proteção contra path traversal durante o `oras pull`.

## Como verificar
Execute `oras push` a partir do diretório raiz dos artefatos usando caminhos relativos limpos e valide a extração com `oras pull -o /tmp/test-pull`.

## Conexões
- [[oras-arquitetura-oci-registry-as-storage-artefatos-genericos]] — Veja também: ORAS: Arquitetura OCI Registry As Storage e Distribuição de Artefatos Genéricos.
- [[oras-attach-discover-grafo-referrers-sbom-assinaturas-oci11]] — Veja também: ORAS: Vinculação e Descoberta de Artefatos na Árvore de Referrers (oras attach e oras discover).

## Fontes
- [ORAS CLI Official Documentation — Commands Reference (push, pull, attach, discover, cp, backup, restore, manifest, blob & repo)](https://oras.land/docs/category/oras-commands/) — Documentação oficial de comandos da CLI do ORAS detalhando manipulação de artefatos, OCI Image Layout (--oci-layout), árvore de referrers OCI 1.1 e cópia recursiva entre registros; consultado em 2026-10-03.
- [ORAS GitHub — README.md (OCI Registry As Storage Overview, Multi-Arch Container Images & Immutable Release Tag Policy)](https://raw.githubusercontent.com/oras-project/oras/main/README.md) — README oficial do oras-project/oras documentando a governança de tags de release (:vX.Y.Z, :vX.Y, :vX, :latest) e instalação; consultado em 2026-10-03.
- [ORAS Project — Official GitHub Repository](https://github.com/oras-project/oras) — Repositório oficial CNCF Sandbox do ORAS; consultado em 2026-10-03.
