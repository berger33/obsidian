---
id: software.devops.tranche14.001378
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

# melange: Assinatura Criptográfica de Pacotes APK (melange keygen, sign-index e --signing-key)

## Em uma frase
Para garantir a autenticidade da cadeia de suprimentos entre o compilador de pacotes e o construtor de imagens, o `melange` gera pares de chaves RSA de 4096 bits (`melange keygen`) e assina tanto cada arquivo `.apk` quanto o índice `APKINDEX.tar.gz` no diretório `packages/<arch>/`.

## Por que importa
Se o diretório local de pacotes gerados no CI não for assinado criptograficamente, o `apko` rejeitará os pacotes por falta de assinatura confiável no keyring.

## Como funciona
Ao executar `melange keygen`, são gerados `melange.rsa` (chave privada) e `melange.rsa.pub` (chave pública); passando `--signing-key melange.rsa` no `melange build`, o pacote e o índice são assinados automaticamente, e `melange.rsa.pub` é informada em `contents.keyring` do `apko.yaml`.

## Exemplo
```bash
melange keygen
melange build melange.yaml --arch x86_64 --signing-key melange.rsa
ls -la packages/x86_64/
```

## Limites e trade-offs
Commitar a chave privada `melange.rsa` no repositório Git permite que qualquer pessoa forje pacotes `.apk` assinados como se fossem do pipeline oficial.

## Como verificar
Mantenha a chave privada de assinatura de produção protegida no cofre do CI/CD (ou gere chaves efêmeras por execução quando o build do `melange` e do `apko` ocorrerem no mesmo job isolado).

## Conexões
- [[melange-test-pipelines-verificacao-funcional-pacotes-subpackages]] — Veja também: melange: Testes Automatizados de Pacotes e Subpacotes (test.pipeline e melange test).
- [[melange-multi-arch-qemu-binfmt-vars-var-transforms]] — Veja também: melange: Compilação Multi-Arquitetura com QEMU e Transformação de Variáveis (vars e var-transforms).

## Fontes
- [melange GitHub — README.md (Declarative APK Package Builder, Pipeline Builds, QEMU Multi-Arch, melange keygen, Default Substitutions & Debugging)](https://raw.githubusercontent.com/chainguard-dev/melange/main/README.md) — README oficial do chainguard-dev/melange documentando o arquivo de build, variáveis de substituição (${{package.*}}, ${{targets.destdir}}), assinatura RSA, subpackages e uso conjunto com apko; consultado em 2026-10-03.
- [melange Official Documentation — docs/BUILD-FILE.md (package, version, epoch, copyright SPDX, dependencies.provides, options & environment)](https://raw.githubusercontent.com/chainguard-dev/melange/main/docs/BUILD-FILE.md) — Especificação oficial do arquivo de build do melange detalhando version/epoch, licenças SPDX em copyright, fluxos de versão com provides e controles do gerador SCA em options; consultado em 2026-10-03.
- [Chainguard melange — Official GitHub Repository](https://github.com/chainguard-dev/melange) — Repositório oficial Apache-2.0 do melange; consultado em 2026-10-03.
