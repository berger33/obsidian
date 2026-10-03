---
id: software.devops.tranche13.001254
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

# ORAS: Cópia de Imagens, Índices Multi-Arch e Grafos de Referrers entre Registries (oras cp)

## Em uma frase
O comando `oras cp` copia artefatos OCI, imagens de containers, índices multi-arquitetura (`OCI Image Index`) e, opcionalmente, toda a árvore de artefatos anexados (`-r` / `--recursive`) de um registro de origem para um registro de destino ou `OCI Image Layout` local.

## Por que importa
Ferramentas tradicionais de `docker pull` seguido de `docker tag` e `docker push` baixam apenas a arquitetura da máquina onde o comando roda e perdem todas as assinaturas, SBOMs e atestações anexadas via OCI Referrers.

## Como funciona
Quando executado como `oras cp -r <origem> <destino>`, o ORAS transfere os blobs e manifestos diretamente entre os endpoints de registry (ou de/para um layout em disco), preservando integralmente os digests SHA-256 de todas as arquiteturas do Image Index e copiando recursivamente cada SBOM e assinatura ligada no grafo de referrers.

## Exemplo
```bash
# Copiar imagem multi-arch junto com todos os seus referrers (SBOMs e assinaturas):
oras cp --recursive \
  ghcr.io/org/service:v2.1.0 \
  registry.internal.corp/prod/service:v2.1.0
```

## Limites e trade-offs
Executar `oras cp` sem a flag `--recursive` (`-r`) ao promover uma imagem de homologação para o registry de produção copia apenas a imagem em si e deixa para trás as assinaturas Notation/Cosign e os SBOMs anexados via `subject`.

## Como verificar
Use sempre `oras cp --recursive` quando promover imagens assinadas entre registros para que os admission controllers (Kyverno/Connaisseur/Ratify) no cluster de destino encontrem as assinaturas.

## Conexões
- [[oras-attach-discover-grafo-referrers-sbom-assinaturas-oci11]] — Veja também: ORAS: Vinculação e Descoberta de Artefatos na Árvore de Referrers (oras attach e oras discover).
- [[oras-backup-restore-arquivamento-portavel-air-gapped]] — Veja também: ORAS: Backup e Restauração de Artefatos e Grafos OCI para Ambientes Air-Gapped (oras backup e oras restore).

## Fontes
- [ORAS CLI Official Documentation — Commands Reference (push, pull, attach, discover, cp, backup, restore, manifest, blob & repo)](https://oras.land/docs/category/oras-commands/) — Documentação oficial de comandos da CLI do ORAS detalhando manipulação de artefatos, OCI Image Layout (--oci-layout), árvore de referrers OCI 1.1 e cópia recursiva entre registros; consultado em 2026-10-03.
- [ORAS GitHub — README.md (OCI Registry As Storage Overview, Multi-Arch Container Images & Immutable Release Tag Policy)](https://raw.githubusercontent.com/oras-project/oras/main/README.md) — README oficial do oras-project/oras documentando a governança de tags de release (:vX.Y.Z, :vX.Y, :vX, :latest) e instalação; consultado em 2026-10-03.
- [ORAS Project — Official GitHub Repository](https://github.com/oras-project/oras) — Repositório oficial CNCF Sandbox do ORAS; consultado em 2026-10-03.
