---
id: software.devops.tranche12.001128
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

# Jetify Devbox: Sistema de Plugins Embutidos e Customizados para Configuração de Pacotes

## Em uma frase
O Devbox inclui um sistema de plugins que é ativado automaticamente quando certos pacotes Nix (como `postgresql`, `mysql`, `nginx`, `redis`, `python`, `poetry` ou `php`) são adicionados ao projeto, criando arquivos de configuração, variáveis de ambiente e serviços locais sem intervenção manual.

## Por que importa
No Nix tradicional, instalar o pacote binário do `postgresql` ou `nginx` não cria automaticamente diretórios de dados graváveis fora da `/nix/store` (que é somente leitura), exigindo scripts manuais complexos para rodar o serviço localmente.

## Como funciona
Ao detectar um pacote com plugin embutido ou declarado no campo `include` do `devbox.json` (`plugin:<nome>` ou caminho local/GitHub), o Devbox instancia templates de configuração dentro de `.devbox/virtenv/<pacote>/`, exporta variáveis como `PGDATA` e `PGHOST` apontando para o diretório do projeto e registra as entradas de `process-compose`.

## Exemplo
```bash
devbox info postgresql
devbox add nginx@latest
ls -la .devbox/virtenv/nginx/
```

## Limites e trade-offs
Modificar arquivos gerados automaticamente dentro de `.devbox/virtenv/` sem mover a configuração para um diretório rastreado pelo projeto faz com que as alterações sejam perdidas quando o ambiente virtual do Devbox é reconstruído (`devbox shell --recompute`).

## Como verificar
Consulte `devbox info <pacote>` para ver quais variáveis de ambiente e arquivos de configuração o plugin expõe e customize apenas os arquivos expostos fora de `.devbox/virtenv/` quando indicado.

## Conexões
- [[devbox-global-substituicao-gerenciador-pacotes-usuario]] — Veja também: Jetify Devbox: Perfil Global (devbox global) para Ferramentas de Linha de Comando do Usuário.
- [[devbox-ci-cd-github-actions-cache-nix-store-determinismo]] — Veja também: Jetify Devbox: Execução de Pipelines CI/CD com devbox run e Cache da Store Nix.

## Fontes
- [Jetify Devbox GitHub — README.md (Isolated Shells, Nix Package Registry, devbox.json & Portable Environments)](https://www.jetify.com/docs/devbox/quickstart) — README oficial do jetify-com/devbox (Apache-2.0) detalhando criação de shells determinísticos sem virtualização pesada, integração com mais de 400.000 versões no Nixhub.io e geração de Dockerfile/devcontainer; consultado em 2026-10-03.
- [Jetify Devbox Official Documentation — Quickstart, Scripts, Services, Direnv & Global Profile](https://raw.githubusercontent.com/jetify-com/devbox/main/README.md) — Guia oficial Quickstart do Devbox documentando devbox init, search, add, shell, devbox.lock, integração com direnv, scripts e perfil global; consultado em 2026-10-03.
- [Jetify Devbox — Official GitHub Repository](https://github.com/jetify-com/devbox) — Repositório oficial do Devbox; consultado em 2026-10-03.
