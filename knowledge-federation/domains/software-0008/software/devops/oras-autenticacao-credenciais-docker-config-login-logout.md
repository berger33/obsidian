---
id: software.devops.tranche13.001260
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

# ORAS: Gerenciamento de Credenciais e Autenticação em Registros OCI (oras login, oras logout e Credential Helpers)

## Em uma frase
Os comandos `oras login` e `oras logout` gerenciam a autenticação contra qualquer registro OCI compatível, integrando-se nativamente ao formato padrão `~/.docker/config.json` e aos credential helpers nativos (`docker-credential-osxkeychain`, `ecr-login`, `gcloud`, `pass`).

## Por que importa
Passar senhas ou Personal Access Tokens diretamente como argumento na linha de comando (`-p SENHA`) expõe a credencial na tabela de processos do sistema (`ps aux`) e no histórico do shell.

## Como funciona
Ao autenticar com `oras login <registry> -u <user> --password-stdin`, o token é lido com segurança do `stdin` e delegado ao credential store configurado; em ambientes sem Docker instalado, o ORAS gerencia as credenciais de forma independente e permite especificar arquivos de configuração isolados por job via flag `--registry-config`.

## Exemplo
```bash
echo "$REGISTRY_TOKEN" | oras login ghcr.io -u "$REGISTRY_USER" --password-stdin --registry-config /tmp/oras-auth.json
oras repo tags ghcr.io/oras-project/oras --registry-config /tmp/oras-auth.json
oras logout ghcr.io --registry-config /tmp/oras-auth.json
```

## Limites e trade-offs
Compartilhar o mesmo `~/.docker/config.json` entre múltiplos jobs concorrentes no mesmo runner de CI faz com que um `oras logout` ao final de um job derrube a sessão de outro job em andamento.

## Como verificar
Em runners compartilhados de CI/CD, passe sempre um caminho exclusivo em `--registry-config` (por exemplo, `$RUNNER_TEMP/oras-config.json`) para isolar as credenciais por execução.

## Conexões
- [[oras-politica-tags-releases-imutaveis-rolling-tags-supply-chain]] — Veja também: ORAS: Governança de Tags de Release (:vX.Y.Z, :vX.Y, :vX e :latest) e Segurança de Supply Chain.

## Fontes
- [ORAS CLI Official Documentation — Commands Reference (push, pull, attach, discover, cp, backup, restore, manifest, blob & repo)](https://oras.land/docs/category/oras-commands/) — Documentação oficial de comandos da CLI do ORAS detalhando manipulação de artefatos, OCI Image Layout (--oci-layout), árvore de referrers OCI 1.1 e cópia recursiva entre registros; consultado em 2026-10-03.
- [ORAS GitHub — README.md (OCI Registry As Storage Overview, Multi-Arch Container Images & Immutable Release Tag Policy)](https://raw.githubusercontent.com/oras-project/oras/main/README.md) — README oficial do oras-project/oras documentando a governança de tags de release (:vX.Y.Z, :vX.Y, :vX, :latest) e instalação; consultado em 2026-10-03.
- [ORAS Project — Official GitHub Repository](https://github.com/oras-project/oras) — Repositório oficial CNCF Sandbox do ORAS; consultado em 2026-10-03.
