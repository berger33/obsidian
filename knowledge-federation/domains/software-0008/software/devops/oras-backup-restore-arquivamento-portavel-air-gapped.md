---
id: software.devops.tranche13.001255
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

# ORAS: Backup e Restauração de Artefatos e Grafos OCI para Ambientes Air-Gapped (oras backup e oras restore)

## Em uma frase
Os subcomandos `oras backup` e `oras restore` permitem exportar artefatos e imagens de um registro remoto para um **OCI Image Layout** empacotado em um diretório local ou arquivo `.tar` autocontido, e restaurá-los posteriormente em outro registro isolado.

## Por que importa
Em instalações on-premises desconectadas da internet (air-gapped), transportar imagens multi-arch junto com seus artefatos anexados usando `docker save` corrompe ou descarta tipos de mídia não-container e referrers OCI 1.1.

## Como funciona
O comando `oras backup --output bundle.tar <registro/repo:tag>` baixa o manifesto (ou índice) e seus blobs para um arquivo tar no formato OCI Image Layout; no ambiente de destino, `oras restore --input bundle.tar <registro-interno/repo:tag>` reconstrói exatamente os mesmos blobs e manifestos no registro privado.

## Exemplo
```bash
oras backup --output release-v1.4.tar ghcr.io/org/platform-bundle:v1.4.0
oras restore --input release-v1.4.tar registry.airgap.local/platform/bundle:v1.4.0
```

## Limites e trade-offs
Modificar arquivos manualmente dentro do tarball gerado por `oras backup` invalida os digests SHA-256 referenciados no `index.json` e nos manifestos internos, fazendo o `oras restore` falhar na verificação de integridade.

## Como verificar
Trate o arquivo `.tar` gerado por `oras backup` como um pacote imutável, verificando seu hash SHA-256 antes de executar `oras restore`.

## Conexões
- [[oras-cp-copia-artefatos-grafos-referrers-entre-registries]] — Veja também: ORAS: Cópia de Imagens, Índices Multi-Arch e Grafos de Referrers entre Registries (oras cp).
- [[oras-manifest-fetch-push-delete-index-multi-arch]] — Veja também: ORAS: Manipulação Direta de Manifestos e Índices OCI (oras manifest fetch, push, index create e update).

## Fontes
- [ORAS CLI Official Documentation — Commands Reference (push, pull, attach, discover, cp, backup, restore, manifest, blob & repo)](https://oras.land/docs/category/oras-commands/) — Documentação oficial de comandos da CLI do ORAS detalhando manipulação de artefatos, OCI Image Layout (--oci-layout), árvore de referrers OCI 1.1 e cópia recursiva entre registros; consultado em 2026-10-03.
- [ORAS GitHub — README.md (OCI Registry As Storage Overview, Multi-Arch Container Images & Immutable Release Tag Policy)](https://raw.githubusercontent.com/oras-project/oras/main/README.md) — README oficial do oras-project/oras documentando a governança de tags de release (:vX.Y.Z, :vX.Y, :vX, :latest) e instalação; consultado em 2026-10-03.
- [ORAS Project — Official GitHub Repository](https://github.com/oras-project/oras) — Repositório oficial CNCF Sandbox do ORAS; consultado em 2026-10-03.
