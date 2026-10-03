---
id: software.devops.tranche09.000855
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/buildpacks/pack/main/README.md", "https://raw.githubusercontent.com/buildpacks/spec/main/platform.md", "https://buildpacks.io/docs/for-app-developers/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Cloud Native Buildpacks: builds reprodutíveis (SOURCE_DATE_EPOCH / --creation-time) e cache granular de camadas

## Em uma frase
Os Cloud Native Buildpacks garantem **Build Reproducibility** zerando timestamps variáveis nas camadas geradas (ou fixando via `--creation-time`) para produzir exatamente o mesmo digest de imagem a partir das mesmas entradas, combinando isso com cache dedicado de compilação e de lançamento.

## Por que importa
Em um `Dockerfile` comum, executar `docker build` duas vezes seguidas sobre exatamente o mesmo código-fonte sem cache gera imagens com digests SHA-256 diferentes porque os timestamps de modificação (`mtime`) dos arquivos e a data de criação no JSON da imagem mudam a cada segundo, dificultando auditorias de cadeia de suprimentos (SLSA) e invalidando caches downstream. A especificação `platform.md` (`Build Reproducibility` e `Caching`) padroniza essa garantia.

## Como funciona
Durante a fase `exporter` do lifecycle: (1) **Reprodutibilidade**: os metadados de tempo de modificação dos arquivos nas camadas criadas pelos buildpacks e a data de criação do manifesto são normalizados para um timestamp fixo determinístico (podendo ser definido ao momento do commit Git ou atual com `pack build --creation-time now`), garantindo que entradas idênticas gerem o mesmo digest SHA-256; e (2) **Caching**: cada subdiretório `<layers>/<layer>` criado por um buildpack pode ser marcado independentemente em `<layer>.toml` com as flags booleanas `build = true` (disponível para buildpacks subsequentes), `cache = true` (persistido no volume/imagem de cache para o `restorer` na próxima compilação, como o repositório `.m2` do Maven) e `launch = true` (incluído na imagem final de produção).

## Exemplo
```bash
# Construir imagem com cache persistido em uma imagem de cache no registry (--cache-image) e timestamp controlado
pack build registry.interno.com/app:v1.0.0 \
  --builder paketobuildpacks/builder-jammy-base \
  --publish \
  --cache-image registry.interno.com/app:cache
```

## Limites e trade-offs
Quando uma camada é marcada pelo buildpack apenas com `cache = true` e `launch = false` (por exemplo, o cache de dependências baixadas do Maven ou do Cargo que já foram linkadas no binário final), ela acelera os próximos builds via `restorer`, mas **não** é enviada para a **App Image** final, mantendo a imagem de produção mínima; já camadas marcadas apenas com `launch = true` e `cache = false` são reaproveitadas pelo `analyzer`/`exporter` diretamente do manifesto da imagem anterior no registry sem precisar trafegar pela rede local.

## Como verificar
Execute `pack build minha-app:repro --builder paketobuildpacks/builder-jammy-base` duas vezes seguidas sem alterar o código nem o builder e confirme com `docker inspect --format '{{.Id}}' minha-app:repro` que o digest da imagem permanece idêntico.

## Conexões
- [[buildpacks-operacao-rebase-atualizacao-rapida-run-image]] — Veja também: Cloud Native Buildpacks: atualização instantânea da imagem base do SO sem recompilar a aplicação (pack rebase).
- [[buildpacks-configuracao-project-toml-env-vars-build]] — Veja também: Cloud Native Buildpacks: configuração declarativa do build com project.toml, variáveis BP_* e BPE_*.
- [[buildpacks-cli-pack-build-lifecycle-builders-oci]] — Referência cruzada direta com buildpacks-cli-pack-build-lifecycle-builders-oci.
- [[buildpacks-fases-lifecycle-analyzer-detector-restorer-builder-exporter]] — Referência cruzada direta com buildpacks-fases-lifecycle-analyzer-detector-restorer-builder-exporter.
- [[nix-gerenciador-pacotes-puramente-funcional-nix-store]] — Referência cruzada direta com nix-gerenciador-pacotes-puramente-funcional-nix-store.

## Fontes
- [Cloud Native Buildpacks pack GitHub — README.md (CLI for App Developers, Buildpack Authors & Platform Operators)](https://raw.githubusercontent.com/buildpacks/pack/main/README.md) — README oficial do buildpacks/pack (projeto CNCF) descrevendo o papel do pack para desenvolvedores, autores de buildpacks e operadores de plataforma; consultado em 2026-10-03.
- [Cloud Native Buildpacks Platform Specification — platform.md (Platform API 0.15, Lifecycle Phases, Rebase, SBOM & Reproducibility)](https://raw.githubusercontent.com/buildpacks/spec/main/platform.md) — Especificação oficial Platform Interface (0.15) definindo Builder, Build Image, Run Image, Launcher, fases detector/analyzer/restorer/extender/builder/exporter/creator/rebaser, Image Extensions, caching, reprodutibilidade, SBOM e transição de stacks para Target Data; consultado em 2026-10-03.
- [Cloud Native Buildpacks — App Developer Guide & Official Repository](https://buildpacks.io/docs/for-app-developers/) — Documentação oficial para desenvolvedores de aplicações e repositório buildpacks/pack; consultado em 2026-10-03.
