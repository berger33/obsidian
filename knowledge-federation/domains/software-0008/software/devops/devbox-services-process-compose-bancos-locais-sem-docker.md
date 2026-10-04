---
id: software.devops.tranche12.001124
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
fontes: ["https://www.jetify.com/docs/devbox/quickstart", "https://raw.githubusercontent.com/jetify-com/devbox/main/README.md", "https://github.com/jetify-com/devbox"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Jetify Devbox: Execução de Serviços em Background (PostgreSQL, Redis, Nginx) sem Docker

## Em uma frase
O Devbox possui gerenciamento integrado de serviços locais (`devbox services up`, `start`, `stop`, `ls`) baseado em `process-compose`, permitindo rodar bancos de dados e daemons como PostgreSQL, Redis ou Nginx nativamente via pacotes Nix sem precisar de Docker Desktop.

## Por que importa
Em laptops corporativos com restrições de licença ou alto consumo de RAM/bateria do Docker Desktop no macOS, subir múltiplos containers apenas para ter um Postgres e um Redis locais degrada a performance de desenvolvimento.

## Como funciona
Quando um pacote com plugin de serviço integrado (como `postgresql` ou `redis`) é adicionado ao `devbox.json`, o Devbox configura automaticamente diretórios locais de dados e sockets dentro de `.devbox/virtenv/` do projeto. O comando `devbox services up` inicia e supervisiona todos os daemons declarados no projeto usando os binários nativos do Nix.

## Exemplo
```bash
devbox add postgresql@15 redis@7.2
devbox run -- initdb
devbox services up -b
devbox services ls
devbox services stop
```

## Limites e trade-offs
Esquecer de adicionar `.devbox/` ao `.gitignore` faz com que diretórios de dados de bancos locais, sockets Unix e caches de pacotes Nix sejam acidentalmente preparados para commit no Git.

## Como verificar
Confirme que `.devbox` está listado no `.gitignore` (o `devbox init` já o gerencia por padrão) e verifique a saúde dos processos em background com `devbox services ls`.

## Conexões
- [[devbox-shell-init-hook-env-scripts-automacao-projeto]] — Veja também: Jetify Devbox: Automação com init_hook, Variáveis env e devbox run Scripts.
- [[devbox-direnv-integracao-ativacao-automatica-diretorio]] — Veja também: Jetify Devbox: Integração com direnv para Ativação Automática ao Entrar no Diretório.

## Fontes
- [Jetify Devbox GitHub — README.md (Isolated Shells, Nix Package Registry, devbox.json & Portable Environments)](https://www.jetify.com/docs/devbox/quickstart) — README oficial do jetify-com/devbox (Apache-2.0) detalhando criação de shells determinísticos sem virtualização pesada, integração com mais de 400.000 versões no Nixhub.io e geração de Dockerfile/devcontainer; consultado em 2026-10-03.
- [Jetify Devbox Official Documentation — Quickstart, Scripts, Services, Direnv & Global Profile](https://raw.githubusercontent.com/jetify-com/devbox/main/README.md) — Guia oficial Quickstart do Devbox documentando devbox init, search, add, shell, devbox.lock, integração com direnv, scripts e perfil global; consultado em 2026-10-03.
- [Jetify Devbox — Official GitHub Repository](https://github.com/jetify-com/devbox) — Repositório oficial do Devbox; consultado em 2026-10-03.
