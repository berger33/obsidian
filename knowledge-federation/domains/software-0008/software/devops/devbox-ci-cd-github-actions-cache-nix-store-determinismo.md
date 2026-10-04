---
id: software.devops.tranche12.001129
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

# Jetify Devbox: Execução de Pipelines CI/CD com devbox run e Cache da Store Nix

## Em uma frase
Usar `devbox run <script>` dentro de pipelines de CI/CD (como GitHub Actions ou GitLab CI) garante que os jobs de lint, teste e build rodem com exatamente os mesmos binários e versões usados localmente pelos desenvolvedores.

## Por que importa
Quando o desenvolvedor testa localmente com `golangci-lint` ou `terraform` instalado via gerenciador de pacotes local e o GitHub Actions usa uma Action terceira com outra versão da ferramenta, surgem falhas que só acontecem na CI.

## Como funciona
No pipeline de CI, instala-se o Devbox (ou usa-se a action oficial `jetify-com/devbox-install-action` com cache da `/nix/store`) e executa-se `devbox run test` e `devbox run build`. O Devbox lê o `devbox.lock` versionado no repositório e restaura os pacotes exatos a partir do cache binário sem divergência.

## Exemplo
```yaml
steps:
  - uses: actions/checkout@v4
  - uses: jetify-com/devbox-install-action@v0.11.0
    with:
      enable-cache: true
  - name: Executar testes e lint no ambiente deterministico
    run: |
      devbox run lint
      devbox run test
```

## Limites e trade-offs
Executar `devbox run` em pipelines de CI efêmeros sem habilitar o cache da `/nix/store` e de `.devbox` força o download completo do catálogo Nix em todo job, adicionando minutos desnecessários ao tempo de build.

## Como verificar
Habilite sempre o cache da store Nix no runner de CI e verifique nos logs do job que os pacotes do `devbox.lock` foram restaurados a partir do cache.

## Conexões
- [[devbox-plugins-sistema-configuracao-automatica-pacotes]] — Veja também: Jetify Devbox: Sistema de Plugins Embutidos e Customizados para Configuração de Pacotes.
- [[devbox-flakes-nixpkgs-custom-outputs-patches-avancado]] — Veja também: Jetify Devbox: Referência Direta a Nix Flakes e Outputs Customizados no devbox.json.

## Fontes
- [Jetify Devbox GitHub — README.md (Isolated Shells, Nix Package Registry, devbox.json & Portable Environments)](https://www.jetify.com/docs/devbox/quickstart) — README oficial do jetify-com/devbox (Apache-2.0) detalhando criação de shells determinísticos sem virtualização pesada, integração com mais de 400.000 versões no Nixhub.io e geração de Dockerfile/devcontainer; consultado em 2026-10-03.
- [Jetify Devbox Official Documentation — Quickstart, Scripts, Services, Direnv & Global Profile](https://raw.githubusercontent.com/jetify-com/devbox/main/README.md) — Guia oficial Quickstart do Devbox documentando devbox init, search, add, shell, devbox.lock, integração com direnv, scripts e perfil global; consultado em 2026-10-03.
- [Jetify Devbox — Official GitHub Repository](https://github.com/jetify-com/devbox) — Repositório oficial do Devbox; consultado em 2026-10-03.
