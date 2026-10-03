---
id: software.devops.tranche12.001123
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

# Jetify Devbox: Automação com init_hook, Variáveis env e devbox run Scripts

## Em uma frase
O arquivo `devbox.json` permite configurar variáveis de ambiente estáticas no bloco `env`, comandos de inicialização automática do shell em `shell.init_hook` e tarefas nomeadas em `shell.scripts` executáveis via `devbox run <script>`.

## Por que importa
Mesmo quando todos os desenvolvedores possuem os mesmos binários instalados, comandos de build, lint e testes continuam falhando se variáveis de ambiente locais ou etapas de preparação (como ativar um virtualenv ou exportar `GOPATH`) não forem padronizadas.

## Como funciona
Sempre que o usuário entra no `devbox shell` ou executa `devbox run <nome-do-script>`, o Devbox injeta as variáveis definidas em `env` (suportando `$PWD` e `$DEVBOX_PROJECT_ROOT`), executa o `init_hook` em um ambiente isolado e roda o script solicitado com exatamente os pacotes declarados no `devbox.json`.

## Exemplo
```json
{
  "packages": ["go@1.22", "golangci-lint@1.57"],
  "env": {
    "CGO_ENABLED": "0",
    "GOFLAGS": "-mod=readonly"
  },
  "shell": {
    "init_hook": ["echo 'Ambiente Go pronto'"],
    "scripts": {
      "lint": ["golangci-lint run ./..."],
      "test": ["go test -race ./..."]
    }
  }
}
```

## Limites e trade-offs
Colocar operações lentas de rede (como downloads pesados ou migrações de banco de dados demoradas) dentro de `shell.init_hook` torna cada abertura de terminal e cada execução de `devbox run` extremamente lenta.

## Como verificar
Mantenha o `init_hook` rápido e idempotente (apenas configuração de shell/ambiente) e mova tarefas pesadas para scripts explícitos em `shell.scripts` acionados sob demanda via `devbox run`.

## Conexões
- [[devbox-search-add-pinning-versoes-nixhub-lockfile]] — Veja também: Jetify Devbox: Busca e Pinagem Exata de Versões de Pacotes com Nixhub e devbox.lock.
- [[devbox-services-process-compose-bancos-locais-sem-docker]] — Veja também: Jetify Devbox: Execução de Serviços em Background (PostgreSQL, Redis, Nginx) sem Docker.

## Fontes
- [Jetify Devbox GitHub — README.md (Isolated Shells, Nix Package Registry, devbox.json & Portable Environments)](https://www.jetify.com/docs/devbox/quickstart) — README oficial do jetify-com/devbox (Apache-2.0) detalhando criação de shells determinísticos sem virtualização pesada, integração com mais de 400.000 versões no Nixhub.io e geração de Dockerfile/devcontainer; consultado em 2026-10-03.
- [Jetify Devbox Official Documentation — Quickstart, Scripts, Services, Direnv & Global Profile](https://raw.githubusercontent.com/jetify-com/devbox/main/README.md) — Guia oficial Quickstart do Devbox documentando devbox init, search, add, shell, devbox.lock, integração com direnv, scripts e perfil global; consultado em 2026-10-03.
- [Jetify Devbox — Official GitHub Repository](https://github.com/jetify-com/devbox) — Repositório oficial do Devbox; consultado em 2026-10-03.
