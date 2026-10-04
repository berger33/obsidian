---
id: software.devops.tranche12.001121
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/jetify-com/devbox/main/README.md", "https://www.jetify.com/docs/devbox/quickstart", "https://github.com/jetify-com/devbox"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Jetify Devbox: Ambientes de Desenvolvimento Reprodutíveis Baseados em Nix (devbox.json)

## Em uma frase
Devbox é uma ferramenta de linha de comando open-source criada pela Jetify que constrói shells e ambientes de desenvolvimento isolados, rápidos e determinísticos a partir de um arquivo declarativo `devbox.json`, utilizando o catálogo de mais de 400.000 versões de pacotes do Nix sem exigir conhecimento da linguagem Nix.

## Por que importa
Instalar ferramentas de projeto diretamente no sistema operacional com `brew` ou `apt-get` polui a máquina local e gera conflitos insolúveis quando dois projetos exigem versões incompatíveis de Python, Go, Terraform, kubectl ou bibliotecas nativas C.

## Como funciona
Com `devbox init` e `devbox add <pacote>@<versao>`, o desenvolvedor declara as dependências de nível de sistema no `devbox.json`. Ao executar `devbox shell` ou `devbox run`, o Devbox resolve as versões exatas via Nixhub.io, registra os hashes criptográficos no `devbox.lock` e monta um shell isolado diretamente no sistema operacional sem a sobrecarga de virtualização de máquinas virtuais ou containers pesados.

## Exemplo
```bash
devbox init
devbox add python@3.10 go@1.22 ripgrep@latest
devbox shell -- python --version
git add devbox.json devbox.lock
```

## Limites e trade-offs
Commitar apenas o `devbox.json` com referências `@latest` e omitir o `devbox.lock` do repositório Git impede que colegas de equipe e agentes de CI reproduzam exatamente os mesmos binários Nix.

## Como verificar
Versione sempre `devbox.json` e `devbox.lock` juntos no Git e verifique as versões ativas dentro do ambiente com `devbox info` e `devbox shell -- which <binario>`.

## Conexões
- [[devbox-search-add-pinning-versoes-nixhub-lockfile]] — Veja também: Jetify Devbox: Busca e Pinagem Exata de Versões de Pacotes com Nixhub e devbox.lock.

## Fontes
- [Jetify Devbox GitHub — README.md (Isolated Shells, Nix Package Registry, devbox.json & Portable Environments)](https://raw.githubusercontent.com/jetify-com/devbox/main/README.md) — README oficial do jetify-com/devbox (Apache-2.0) detalhando criação de shells determinísticos sem virtualização pesada, integração com mais de 400.000 versões no Nixhub.io e geração de Dockerfile/devcontainer; consultado em 2026-10-03.
- [Jetify Devbox Official Documentation — Quickstart, Scripts, Services, Direnv & Global Profile](https://www.jetify.com/docs/devbox/quickstart) — Guia oficial Quickstart do Devbox documentando devbox init, search, add, shell, devbox.lock, integração com direnv, scripts e perfil global; consultado em 2026-10-03.
- [Jetify Devbox — Official GitHub Repository](https://github.com/jetify-com/devbox) — Repositório oficial do Devbox; consultado em 2026-10-03.
