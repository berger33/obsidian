---
id: software.devops.tranche12.001122
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

# Jetify Devbox: Busca e Pinagem Exata de Versões de Pacotes com Nixhub e devbox.lock

## Em uma frase
Diferente do comando `nix-env` tradicional que exige localizar hashes de commits do repositório `nixpkgs`, o Devbox permite pesquisar e fixar versões semânticas legíveis (`<pacote>@<versao>`) consultando o índice Nixhub.io e travando a resolução no `devbox.lock`.

## Por que importa
Equipes que adotam Nix puro frequentemente enfrentam atrito severo quando precisam fixar uma versão específica de um compilador ou CLI antiga sem atualizar toda a árvore `nixpkgs` do projeto.

## Como funciona
O comando `devbox search <termo>` consulta as versões disponíveis no catálogo; em seguida, `devbox add nodejs@20.11.0` ou `devbox add postgresql@15` adiciona a restrição ao array `packages` do `devbox.json` e grava no `devbox.lock` a URL exata da store Nix e o hash de integridade para cada arquitetura suportada (`x86_64-linux`, `aarch64-darwin`, etc.).

## Exemplo
```bash
devbox search kubectl
devbox add kubectl@1.29 helm@3.14 jq@1.7
cat devbox.json
cat devbox.lock
```

## Limites e trade-offs
Editar manualmente os hashes dentro de `devbox.lock` ou remover pacotes diretamente do JSON sem rodar `devbox rm` ou `devbox update` deixa entradas órfãs ou inconsistentes no lockfile.

## Como verificar
Use sempre `devbox add`, `devbox rm` e `devbox update` para manipular pacotes e confirme que `devbox shell -- <cmd> --version` reflete a versão exata pinada.

## Conexões
- [[devbox-ambientes-desenvolvimento-reprodutiveis-nix-devbox-json]] — Veja também: Jetify Devbox: Ambientes de Desenvolvimento Reprodutíveis Baseados em Nix (devbox.json).
- [[devbox-shell-init-hook-env-scripts-automacao-projeto]] — Veja também: Jetify Devbox: Automação com init_hook, Variáveis env e devbox run Scripts.

## Fontes
- [Jetify Devbox GitHub — README.md (Isolated Shells, Nix Package Registry, devbox.json & Portable Environments)](https://www.jetify.com/docs/devbox/quickstart) — README oficial do jetify-com/devbox (Apache-2.0) detalhando criação de shells determinísticos sem virtualização pesada, integração com mais de 400.000 versões no Nixhub.io e geração de Dockerfile/devcontainer; consultado em 2026-10-03.
- [Jetify Devbox Official Documentation — Quickstart, Scripts, Services, Direnv & Global Profile](https://raw.githubusercontent.com/jetify-com/devbox/main/README.md) — Guia oficial Quickstart do Devbox documentando devbox init, search, add, shell, devbox.lock, integração com direnv, scripts e perfil global; consultado em 2026-10-03.
- [Jetify Devbox — Official GitHub Repository](https://github.com/jetify-com/devbox) — Repositório oficial do Devbox; consultado em 2026-10-03.
