---
id: software.devops.tranche12.001127
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

# Jetify Devbox: Perfil Global (devbox global) para Ferramentas de Linha de Comando do Usuário

## Em uma frase
Além de ambientes por projeto, o modo `devbox global` permite gerenciar ferramentas de uso diário do engenheiro (como `ripgrep`, `jq`, `kubectl`, `stern`, `gh` e `lazygit`) em um perfil global declarativo e portável entre máquinas macOS e Linux.

## Por que importa
Quando um engenheiro troca de estação de trabalho ou alterna entre macOS e Linux, scripts de bootstrap baseados em `Homebrew` ou `apt` instalam versões diferentes de utilitários de CLI ou falham por diferenças de nomes de pacotes entre distros.

## Como funciona
Com `devbox global add <pacote>`, os pacotes são registrados num manifesto `devbox.json` global (em `~/.local/share/devbox/global/default/`). Ao adicionar `eval "$(devbox global shellenv)"` ao `.bashrc` ou `.zshrc`, todas as ferramentas globais ficam disponíveis no `PATH` do usuário e podem ser sincronizadas entre máquinas via `devbox global push` e `devbox global pull`.

## Exemplo
```bash
devbox global add ripgrep@latest jq@1.7 gh@latest
eval "$(devbox global shellenv)"
devbox global list
```

## Limites e trade-offs
Instalar compiladores e runtimes específicos de aplicação (como versões fixas de Node.js ou Python de um único serviço) no `devbox global` em vez do `devbox.json` do projeto esconde dependências que deveriam estar versionadas no repositório da aplicação.

## Como verificar
Use `devbox global` exclusivamente para utilitários de produtividade pessoal do operador e mantenha todas as dependências de build/teste declaradas no `devbox.json` local de cada repositório.

## Conexões
- [[devbox-generate-dockerfile-devcontainer-portabilidade-producao]] — Veja também: Jetify Devbox: Geração de Dockerfile e Devcontainer a partir do devbox.json.
- [[devbox-plugins-sistema-configuracao-automatica-pacotes]] — Veja também: Jetify Devbox: Sistema de Plugins Embutidos e Customizados para Configuração de Pacotes.

## Fontes
- [Jetify Devbox GitHub — README.md (Isolated Shells, Nix Package Registry, devbox.json & Portable Environments)](https://www.jetify.com/docs/devbox/quickstart) — README oficial do jetify-com/devbox (Apache-2.0) detalhando criação de shells determinísticos sem virtualização pesada, integração com mais de 400.000 versões no Nixhub.io e geração de Dockerfile/devcontainer; consultado em 2026-10-03.
- [Jetify Devbox Official Documentation — Quickstart, Scripts, Services, Direnv & Global Profile](https://raw.githubusercontent.com/jetify-com/devbox/main/README.md) — Guia oficial Quickstart do Devbox documentando devbox init, search, add, shell, devbox.lock, integração com direnv, scripts e perfil global; consultado em 2026-10-03.
- [Jetify Devbox — Official GitHub Repository](https://github.com/jetify-com/devbox) — Repositório oficial do Devbox; consultado em 2026-10-03.
