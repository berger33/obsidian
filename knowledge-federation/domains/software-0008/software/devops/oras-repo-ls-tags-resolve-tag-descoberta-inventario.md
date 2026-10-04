---
id: software.devops.tranche13.001258
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

# ORAS: Descoberta de Repositórios, Tags e Resolução de Digests (oras repo ls, oras repo tags, oras resolve e oras tag)

## Em uma frase
Para navegação, inventário e promoção de tags sem download de dados, o ORAS disponibiliza `oras repo ls`, `oras repo tags`, `oras resolve` e `oras tag`.

## Por que importa
Em scripts de automação de deploy e promoção GitOps, usar clientes pesados apenas para descobrir qual é o digest SHA-256 atual de uma tag ou adicionar uma tag `:prod` a um manifesto já existente no registry é ineficiente.

## Como funciona
O comando `oras repo ls <registro>` enumera os repositórios via API de catálogo; `oras repo tags <registro/repo>` lista todas as tags disponíveis; `oras resolve <registro/repo:tag>` resolve rapidamente a tag para seu digest imutável `sha256:...` via requisição `HEAD`; e `oras tag <registro/repo:tag-origem> <nova-tag>` aplica novas tags remotamente.

## Exemplo
```bash
DIGEST=$(oras resolve ghcr.io/oras-project/oras:v1.2.0)
echo "Digest imutavel: $DIGEST"
oras repo tags ghcr.io/oras-project/oras | tail -n 5
```

## Limites e trade-offs
Depender de `oras repo ls` em registros públicos massivos (como Docker Hub ou GHCR) falha porque grandes registros multi-tenant desabilitam o endpoint global `/v2/_catalog` por motivos de segurança e escala.

## Como verificar
Use `oras repo ls` em registros privados corporativos (Harbor, Zot, Distribution) e utilize `oras repo tags` e `oras resolve` diretamente nos repositórios conhecidos em registros públicos.

## Conexões
- [[oras-blob-fetch-push-delete-operacoes-camada-digest]] — Veja também: ORAS: Operações Diretas em Blobs Endereçáveis por Conteúdo (oras blob push, fetch e delete).
- [[oras-politica-tags-releases-imutaveis-rolling-tags-supply-chain]] — Veja também: ORAS: Governança de Tags de Release (:vX.Y.Z, :vX.Y, :vX e :latest) e Segurança de Supply Chain.

## Fontes
- [ORAS CLI Official Documentation — Commands Reference (push, pull, attach, discover, cp, backup, restore, manifest, blob & repo)](https://oras.land/docs/category/oras-commands/) — Documentação oficial de comandos da CLI do ORAS detalhando manipulação de artefatos, OCI Image Layout (--oci-layout), árvore de referrers OCI 1.1 e cópia recursiva entre registros; consultado em 2026-10-03.
- [ORAS GitHub — README.md (OCI Registry As Storage Overview, Multi-Arch Container Images & Immutable Release Tag Policy)](https://raw.githubusercontent.com/oras-project/oras/main/README.md) — README oficial do oras-project/oras documentando a governança de tags de release (:vX.Y.Z, :vX.Y, :vX, :latest) e instalação; consultado em 2026-10-03.
- [ORAS Project — Official GitHub Repository](https://github.com/oras-project/oras) — Repositório oficial CNCF Sandbox do ORAS; consultado em 2026-10-03.
