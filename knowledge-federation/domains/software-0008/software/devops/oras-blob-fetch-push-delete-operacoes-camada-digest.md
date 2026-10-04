---
id: software.devops.tranche13.001257
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

# ORAS: Operações Diretas em Blobs Endereçáveis por Conteúdo (oras blob push, fetch e delete)

## Em uma frase
Os subcomandos `oras blob` (`oras blob push`, `oras blob fetch` e `oras blob delete`) permitem interagir diretamente com o armazenamento endereçável por conteúdo (`/v2/<name>/blobs/<digest>`) de um registry OCI sem precisar construir um manifesto completo.

## Por que importa
Ao construir pipelines customizados de montagem de imagens ou inspecionar uma única camada/artefato específico dentro de um manifesto de múltiplos blobs, baixar a imagem inteira desperdiça tempo e banda.

## Como funciona
Com `oras blob fetch --output camada.tar.gz <registro/repo@sha256:...>`, o cliente baixa e verifica o hash de um único blob específico. Com `oras blob push <registro/repo> arquivo.bin`, o blob é enviado ao repositório e seu descritor OCI JSON (`mediaType`, `digest`, `size`) pode ser emitido com `--descriptor` para inclusão posterior em um `oras manifest push`.

## Exemplo
```bash
oras blob push --descriptor localhost:5000/artifacts/data ./payload.json
oras blob fetch --output /tmp/payload.json \
  localhost:5000/artifacts/data@sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

## Limites e trade-offs
Enviar um blob com `oras blob push` e nunca referenciá-lo em um manifesto publicado com `oras manifest push` deixa o blob órfão no repositório, sujeito a remoção pelo coletor de lixo (Garbage Collector) do registry.

## Como verificar
Vincule todo blob enviado avulsamente a um manifesto ativo via `oras manifest push` dentro da janela de retenção (`gcDelay`) do registro.

## Conexões
- [[oras-manifest-fetch-push-delete-index-multi-arch]] — Veja também: ORAS: Manipulação Direta de Manifestos e Índices OCI (oras manifest fetch, push, index create e update).
- [[oras-repo-ls-tags-resolve-tag-descoberta-inventario]] — Veja também: ORAS: Descoberta de Repositórios, Tags e Resolução de Digests (oras repo ls, oras repo tags, oras resolve e oras tag).

## Fontes
- [ORAS CLI Official Documentation — Commands Reference (push, pull, attach, discover, cp, backup, restore, manifest, blob & repo)](https://oras.land/docs/category/oras-commands/) — Documentação oficial de comandos da CLI do ORAS detalhando manipulação de artefatos, OCI Image Layout (--oci-layout), árvore de referrers OCI 1.1 e cópia recursiva entre registros; consultado em 2026-10-03.
- [ORAS GitHub — README.md (OCI Registry As Storage Overview, Multi-Arch Container Images & Immutable Release Tag Policy)](https://raw.githubusercontent.com/oras-project/oras/main/README.md) — README oficial do oras-project/oras documentando a governança de tags de release (:vX.Y.Z, :vX.Y, :vX, :latest) e instalação; consultado em 2026-10-03.
- [ORAS Project — Official GitHub Repository](https://github.com/oras-project/oras) — Repositório oficial CNCF Sandbox do ORAS; consultado em 2026-10-03.
