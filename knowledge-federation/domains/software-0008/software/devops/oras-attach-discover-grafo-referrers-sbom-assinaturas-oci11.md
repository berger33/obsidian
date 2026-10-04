---
id: software.devops.tranche13.001253
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

# ORAS: Vinculação e Descoberta de Artefatos na Árvore de Referrers (oras attach e oras discover)

## Em uma frase
Os comandos `oras attach` e `oras discover` implementam o grafo de **Referrers da especificação OCI 1.1** (`subject`), permitindo anexar SBOMs, relatórios de vulnerabilidades Trivy, atestações SLSA e assinaturas diretamente a uma imagem de container existente sem alterar o digest da imagem.

## Por que importa
Se o SBOM ou o relatório de scan de segurança for salvo em um repositório separado ou com uma tag solta, torna-se difícil provar criptograficamente a qual digest exato de imagem de container aquele SBOM pertence.

## Como funciona
Ao executar `oras attach --artifact-type application/spdx+json <imagem@sha256:...> sbom.spdx.json`, o ORAS faz push do novo artefato contendo o campo `subject` apontando para o descritor da imagem alvo. Posteriormente, `oras discover <imagem@sha256:...>` consulta a API de Referrers do registry e exibe em árvore (ou JSON/tabela) todos os artefatos anexados àquela imagem.

## Exemplo
```bash
IMAGE="ghcr.io/org/api@sha256:4a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b"
oras attach --artifact-type application/vnd.cyclonedx+json "$IMAGE" ./sbom.cdx.json:application/json
oras discover "$IMAGE" --format tree
```

## Limites e trade-offs
Anexar artefatos com `oras attach` referenciando uma tag mutável (`:latest`) sem registrar o digest imutável resolvido pode causar confusão quando a tag `:latest` for movida para outra imagem.

## Como verificar
Passe sempre a referência imutável por digest (`@sha256:...`) nos comandos `oras attach` e `oras discover`.

## Conexões
- [[oras-push-pull-media-types-annotations-oci-image-layout]] — Veja também: ORAS: Operações de Push e Pull de Arquivos, Media Types, Anotações e OCI Image Layout Local.
- [[oras-cp-copia-artefatos-grafos-referrers-entre-registries]] — Veja também: ORAS: Cópia de Imagens, Índices Multi-Arch e Grafos de Referrers entre Registries (oras cp).

## Fontes
- [ORAS CLI Official Documentation — Commands Reference (push, pull, attach, discover, cp, backup, restore, manifest, blob & repo)](https://oras.land/docs/category/oras-commands/) — Documentação oficial de comandos da CLI do ORAS detalhando manipulação de artefatos, OCI Image Layout (--oci-layout), árvore de referrers OCI 1.1 e cópia recursiva entre registros; consultado em 2026-10-03.
- [ORAS GitHub — README.md (OCI Registry As Storage Overview, Multi-Arch Container Images & Immutable Release Tag Policy)](https://raw.githubusercontent.com/oras-project/oras/main/README.md) — README oficial do oras-project/oras documentando a governança de tags de release (:vX.Y.Z, :vX.Y, :vX, :latest) e instalação; consultado em 2026-10-03.
- [ORAS Project — Official GitHub Repository](https://github.com/oras-project/oras) — Repositório oficial CNCF Sandbox do ORAS; consultado em 2026-10-03.
