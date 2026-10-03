---
id: software.devops.tranche12.001130
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

# Jetify Devbox: Referência Direta a Nix Flakes e Outputs Customizados no devbox.json

## Em uma frase
Embora abstraia o Nix para o caso de uso comum, o Devbox permite referenciar diretamente Nix Flakes arbitrários (locais ou remotos via `github:org/repo#output`), selecionar `outputs` adicionais (como headers `dev` ou manpages) e excluir pacotes conflitantes na configuração avançada do `devbox.json`.

## Por que importa
Projetos que compilam extensões nativas C/C++ ou dependem de ferramentas internas distribuídas como Nix Flakes privados precisam combinar a simplicidade do `devbox.json` com o poder completo de seleção de outputs da store Nix.

## Como funciona
No `devbox.json`, entradas em `packages` podem usar a sintaxe de objeto detalhado ou URIs de Flake (`path:./meu-flake#minha-cli` ou `github:nixos/nixpkgs/nixos-23.11#hello`), além de especificar `outputs: ["out", "dev"]` para disponibilizar cabeçalhos de compilação (`CFLAGS`/`PKG_CONFIG_PATH`) no shell isolado.

## Exemplo
```json
{
  "packages": {
    "openssl": {
      "version": "3.0",
      "outputs": ["out", "dev"]
    },
    "custom-cli": "github:my-org/internal-tools/v1.4.0#custom-cli"
  }
}
```

## Limites e trade-offs
Referenciar Flakes GitHub por nome de branch mutável (`github:org/repo/main#pkg`) sem commitar o `devbox.lock` atualizado permite que mudanças upstream quebrem o build de outros desenvolvedores.

## Como verificar
Sempre fixe tags ou commits imutáveis ao referenciar Flakes externos e execute `devbox update` de maneira controlada em Pull Requests dedicados.

## Conexões
- [[devbox-ci-cd-github-actions-cache-nix-store-determinismo]] — Veja também: Jetify Devbox: Execução de Pipelines CI/CD com devbox run e Cache da Store Nix.

## Fontes
- [Jetify Devbox GitHub — README.md (Isolated Shells, Nix Package Registry, devbox.json & Portable Environments)](https://www.jetify.com/docs/devbox/quickstart) — README oficial do jetify-com/devbox (Apache-2.0) detalhando criação de shells determinísticos sem virtualização pesada, integração com mais de 400.000 versões no Nixhub.io e geração de Dockerfile/devcontainer; consultado em 2026-10-03.
- [Jetify Devbox Official Documentation — Quickstart, Scripts, Services, Direnv & Global Profile](https://raw.githubusercontent.com/jetify-com/devbox/main/README.md) — Guia oficial Quickstart do Devbox documentando devbox init, search, add, shell, devbox.lock, integração com direnv, scripts e perfil global; consultado em 2026-10-03.
- [Jetify Devbox — Official GitHub Repository](https://github.com/jetify-com/devbox) — Repositório oficial do Devbox; consultado em 2026-10-03.
