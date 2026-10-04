---
id: software.devops.tranche10.000964
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/goreleaser/goreleaser/main/README.md", "https://goreleaser.com/getting-started/quick-start/", "https://github.com/goreleaser/goreleaser"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# GoReleaser: empacotamento em arquivos (.tar.gz/.zip), pacotes Linux via nFPM (.deb, .rpm, .apk) e gerenciadores (Homebrew/Scoop/Winget)

## Em uma frase
Após compilar os binários, o GoReleaser cria arquivos compactados por plataforma na seção **`archives:`**, gera pacotes nativos de distribuições Linux (`.deb`, `.rpm`, `.apk`, `.archlinux`) sem precisar de ferramentas específicas da distro via **`nfpms:`** e publica fórmulas/manifestos para **Homebrew**, **Scoop**, **Winget**, **AUR** e **Snapcraft**.

## Por que importa
Usuários de macOS esperam instalar sua ferramenta com `brew install sua-org/tap/sua-cli`, usuários de Ubuntu/Debian querem um pacote `.deb`, usuários de RHEL/Fedora querem um `.rpm` e usuários de Windows querem `.zip`, `scoop` ou `winget`. Manter pipelines separados em máquinas diferentes para criar pacotes `.deb` e `.rpm` é complexo; o **nFPM** embutido no GoReleaser gera todos eles em puro Go em qualquer SO.

## Como funciona
No `.goreleaser.yaml`: (1) **`archives:`**: empacota o binário de cada alvo junto com `README.md`, `LICENSE` e scripts de autocompletar em `.tar.gz` (ou `.zip` para Windows via `format_overrides`, ou publica o binário puro com `formats: [binary]`); (2) **`nfpms:`**: utiliza a biblioteca Go `goreleaser/nfpm` para construir pacotes `.deb`, `.rpm`, `.apk` (Alpine) e `.archlinux` definindo `maintainer`, `description`, `license`, `dependencies`, arquivos de configuração (`/etc/...`) e scripts de `postinstall`; e (3) **`brews:` / `scoops:` / `winget:`**: commita automaticamente a fórmula Ruby ou manifesto JSON atualizado em um repositório Git de `homebrew-tap` ou `scoop-bucket` apontando para as URLs e hashes SHA-256 da nova release.

## Exemplo
```yaml
# Exemplo de configuração archives e nfpms no .goreleaser.yaml para gerar tar.gz, zip no Windows e pacotes .deb/.rpm
archives:
  - formats: [tar.gz]
    format_overrides:
      - goos: windows
        formats: [zip]
nfpms:
  - package_name: minha-cli
    vendor: Minha Org
    homepage: https://exemplo.com
    maintainer: DevOps <devops@exemplo.com>
    formats:
      - deb
      - rpm
      - apk
```

## Limites e trade-offs
Para que o GoReleaser consiga fazer push automático da fórmula do Homebrew (`brews:`) para um **outro** repositório Git (como `github.com/sua-org/homebrew-tap`), o `GITHUB_TOKEN` padrão gerado automaticamente pelo GitHub Actions para o repositório atual não terá permissão de escrita no repositório `homebrew-tap`; você precisará configurar um Personal Access Token (ou GitHub App Token) com permissão `contents: write` no repositório do tap.

## Como verificar
Execute `goreleaser release --snapshot --clean` com a seção `nfpms` ativa e verifique na pasta `./dist` a criação dos pacotes `.deb`, `.rpm` e `.apk` prontos para instalação.

## Conexões
- [[goreleaser-configuracao-builds-matriz-ldflags-env-hooks]] — Veja também: GoReleaser: customização da seção builds (goos, goarch, env, flags, ldflags e hooks de pré/pós-build).
- [[goreleaser-seguranca-checksums-sbom-syft-assinatura-cosign]] — Veja também: GoReleaser: segurança de cadeia de suprimentos com checksums SHA-256, geração de SBOM (Syft) e assinatura (Cosign / GPG).
- [[goreleaser-automacao-release-engineering-multilinguagem]] — Referência cruzada direta com goreleaser-automacao-release-engineering-multilinguagem.
- [[nix-gerenciador-pacotes-puramente-funcional-nix-store]] — Referência cruzada direta com nix-gerenciador-pacotes-puramente-funcional-nix-store.

## Fontes
- [GoReleaser Official Documentation — Quick Start (goreleaser init, check, healthcheck, build --single-target, release --snapshot & GITHUB_TOKEN)](https://raw.githubusercontent.com/goreleaser/goreleaser/main/README.md) — Guia oficial Quick Start do GoReleaser (v2.18+) demonstrando inicialização, builders para Go/Rust/Node.js/Zig/Bun/Deno/uv/Poetry, --snapshot, --single-target, check, healthcheck, --skip=publish e permissões GITHUB_TOKEN; consultado em 2026-10-03.
- [GoReleaser GitHub — README.md (Release Engineering Automation & Multi-Language Support)](https://goreleaser.com/getting-started/quick-start/) — README oficial do projeto goreleaser/goreleaser (MIT); consultado em 2026-10-03.
- [GoReleaser — Official GitHub Repository](https://github.com/goreleaser/goreleaser) — Repositório oficial do GoReleaser; consultado em 2026-10-03.
