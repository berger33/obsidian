---
id: software.devops.tranche13.001259
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
fontes: ["https://raw.githubusercontent.com/oras-project/oras/main/README.md", "https://oras.land/docs/category/oras-commands/", "https://github.com/oras-project/oras"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# ORAS: Governança de Tags de Release (:vX.Y.Z, :vX.Y, :vX e :latest) e Segurança de Supply Chain

## Em uma frase
O próprio projeto ORAS implementa e documenta uma política rigorosa de publicação de imagens multi-arquitetura no GitHub Container Registry (`ghcr.io/oras-project/oras`) que separa tags de versão imutáveis (`:vX.Y.Z`) de tags rolantes limitadas por linha (`:vX.Y`, `:vX`, `:latest`, `:main`).

## Por que importa
Em muitos projetos open-source e internos, publicar um patch de manutenção em uma versão antiga (por exemplo, `v1.1.5` após a `v1.2.0` já existir) move acidentalmente a tag `:latest` ou `:v1` para trás se o pipeline de release não comparar a ordem semântica das versões.

## Como funciona
Conforme documentado no ORAS, pré-releases nunca movem tags rolantes, e uma release em branch de manutenção só atualiza as tags rolantes de sua própria linha minor (`:vX.Y`) e major (`:vX`) quando for estritamente mais nova do que a versão atualmente apontada, impedindo que backports façam `:latest` regredir.

## Exemplo
```bash
# Fixar a versao exata da imagem do ORAS CLI em pipelines CI/CD:
docker run --rm ghcr.io/oras-project/oras:v1.2.0 version
```

## Limites e trade-offs
Usar a tag `:main` (que acompanha cada merge na branch principal de desenvolvimento) em pipelines de produção expõe a automação a mudanças não lançadas oficialmente.

## Como verificar
Em pipelines de produção, fixe sempre a tag imutável `:vX.Y.Z` (ou digest `@sha256:...`) de `ghcr.io/oras-project/oras`.

## Conexões
- [[oras-repo-ls-tags-resolve-tag-descoberta-inventario]] — Veja também: ORAS: Descoberta de Repositórios, Tags e Resolução de Digests (oras repo ls, oras repo tags, oras resolve e oras tag).
- [[oras-autenticacao-credenciais-docker-config-login-logout]] — Veja também: ORAS: Gerenciamento de Credenciais e Autenticação em Registros OCI (oras login, oras logout e Credential Helpers).

## Fontes
- [ORAS CLI Official Documentation — Commands Reference (push, pull, attach, discover, cp, backup, restore, manifest, blob & repo)](https://raw.githubusercontent.com/oras-project/oras/main/README.md) — Documentação oficial de comandos da CLI do ORAS detalhando manipulação de artefatos, OCI Image Layout (--oci-layout), árvore de referrers OCI 1.1 e cópia recursiva entre registros; consultado em 2026-10-03.
- [ORAS GitHub — README.md (OCI Registry As Storage Overview, Multi-Arch Container Images & Immutable Release Tag Policy)](https://oras.land/docs/category/oras-commands/) — README oficial do oras-project/oras documentando a governança de tags de release (:vX.Y.Z, :vX.Y, :vX, :latest) e instalação; consultado em 2026-10-03.
- [ORAS Project — Official GitHub Repository](https://github.com/oras-project/oras) — Repositório oficial CNCF Sandbox do ORAS; consultado em 2026-10-03.
