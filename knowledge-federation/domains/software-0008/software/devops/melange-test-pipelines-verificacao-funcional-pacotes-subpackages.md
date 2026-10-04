---
id: software.devops.tranche14.001377
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/chainguard-dev/melange/main/README.md", "https://raw.githubusercontent.com/chainguard-dev/melange/main/docs/BUILD-FILE.md", "https://github.com/chainguard-dev/melange"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# melange: Testes Automatizados de Pacotes e Subpacotes (test.pipeline e melange test)

## Em uma frase
O `melange` suporta blocos declarativos `test:` tanto no nível raiz do pacote quanto dentro de cada item de `subpackages`, executados com o comando `melange test` em um ambiente limpo que instala apenas o pacote recém-construído e suas dependências de runtime.

## Por que importa
Um pacote `.apk` pode compilar com código de saída `0`, mas falhar em tempo de execução no container final porque faltou declarar uma dependência de runtime não-ELF (como um script Python, certificado CA ou arquivo de dados).

## Como funciona
Durante `melange test`, o `melange` cria um container isolado contendo apenas o pacote alvo, suas dependências `runtime` declaradas e os pacotes extras listados em `test.environment.contents.packages`, executando os comandos de validação em `test.pipeline` (como `hello --version` ou `uses: test/docs`).

## Exemplo
```yaml
test:
  environment:
    contents:
      packages:
        - busybox
  pipeline:
    - runs: |
        hello
        hello --version
```

## Limites e trade-offs
Incluir todos os pacotes de compilação em `test.environment.contents.packages` mascara dependências de runtime ausentes que só falharão quando o pacote for instalado sozinho pelo `apko`.

## Como verificar
Mantenha `test.environment.contents.packages` mínimo para que `melange test` valide fielmente se `package.dependencies.runtime` está completo.

## Conexões
- [[melange-dependencies-runtime-provides-version-streams-sca]] — Veja também: melange: Resolução Automática de Dependências (SCA), provides para Version Streams e options.
- [[melange-assinatura-rsa-keygen-apkindex-repositorio-local]] — Veja também: melange: Assinatura Criptográfica de Pacotes APK (melange keygen, sign-index e --signing-key).

## Fontes
- [melange GitHub — README.md (Declarative APK Package Builder, Pipeline Builds, QEMU Multi-Arch, melange keygen, Default Substitutions & Debugging)](https://raw.githubusercontent.com/chainguard-dev/melange/main/README.md) — README oficial do chainguard-dev/melange documentando o arquivo de build, variáveis de substituição (${{package.*}}, ${{targets.destdir}}), assinatura RSA, subpackages e uso conjunto com apko; consultado em 2026-10-03.
- [melange Official Documentation — docs/BUILD-FILE.md (package, version, epoch, copyright SPDX, dependencies.provides, options & environment)](https://raw.githubusercontent.com/chainguard-dev/melange/main/docs/BUILD-FILE.md) — Especificação oficial do arquivo de build do melange detalhando version/epoch, licenças SPDX em copyright, fluxos de versão com provides e controles do gerador SCA em options; consultado em 2026-10-03.
- [Chainguard melange — Official GitHub Repository](https://github.com/chainguard-dev/melange) — Repositório oficial Apache-2.0 do melange; consultado em 2026-10-03.
