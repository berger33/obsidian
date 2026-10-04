---
id: software.devops.tranche16.001532
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://carvel.dev/imgpkg/docs/v0.43.x/resources/", "https://raw.githubusercontent.com/carvel-dev/imgpkg/develop/README.md", "https://github.com/carvel-dev/imgpkg"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel imgpkg: estrutura e restrições do diretório `.imgpkg/` (`images.yml` e `bundle.yml`)

## Em uma frase
Todo Bundle do `imgpkg` é governado pelo diretório de metadados `.imgpkg/`, que exige o arquivo `images.yml` (`kind: ImagesLock`) e aceita opcionalmente `bundle.yml` (`kind: Bundle`) com metadados de autoria e websites.

## Por que importa
Para que ferramentas automatizadas e operadores (como o `kapp-controller`) consumam qualquer bundle de forma previsível e saibam exatamente quais imagens OCI precisam ser copiadas ou reescritas, a localização e o esquema dos metadados do bundle precisam ser estritamente padronizados.

## Como funciona
O arquivo `.imgpkg/images.yml` (`apiVersion: imgpkg.carvel.dev/v1alpha1`, `kind: ImagesLock`) lista 0 ou mais imagens dependentes exclusivamente por digest (`image: repo@sha256:...`) e suas `annotations` (como `kbld.carvel.dev/id`). O `imgpkg` impõe duas restrições estruturais no `push`: apenas um único diretório `.imgpkg` pode existir entre todos os diretórios passados via `-f`, e ele deve ser filho direto de um dos diretórios de entrada.

## Exemplo
```yaml
# .imgpkg/bundle.yml
apiVersion: imgpkg.carvel.dev/v1alpha1
kind: Bundle
metadata:
  name: payments-platform
authors:
  - name: Platform Engineering Team
    email: platform@example.com
websites:
  - url: internal.docs.example.com/payments
```

## Limites e trade-offs
Se o arquivo `.imgpkg/images.yml` contiver uma referência de imagem por tag (como `nginx:1.25`) sem `@sha256:...`, o comando `imgpkg push -b` rejeitará o bundle imediatamente por violação da especificação `ImagesLock`.

## Como verificar
Valide a presença de `.imgpkg/images.yml` como filho direto do diretório raiz do pacote e execute `imgpkg push -b registry.example.com/app/bundle:v1 -f .` para testar o contrato.

## Conexões
- [[carvel-imgpkg-conceito-oci-bundle-arquivos-imagens-dependentes]] — Veja também: Carvel imgpkg: empacotamento de configurações e referências de imagens em OCI Bundles imutáveis.
- [[carvel-imgpkg-copy-relocacao-espessa-registries-air-gapped-tar]] — Veja também: Carvel imgpkg: cópia espessa (*thick copy*) de bundles e imagens dependentes entre registries e tarballs air-gapped.

## Fontes
- [Carvel imgpkg GitHub — README.md (OCI Bundles, Thick Copy, Air-Gapped Relocation & Deterministic Layers)](https://carvel.dev/imgpkg/docs/v0.43.x/resources/) — README oficial do carvel-dev/imgpkg apresentando o conceito de OCI Bundle, comandos push/pull/copy e suporte a ambientes air-gapped; consultado em 2026-10-03.
- [Carvel imgpkg Official Documentation — Resources v0.43.x (Bundle, .imgpkg Directory, ImagesLock, BundleLock, Nested Bundles & ImageLocations)](https://raw.githubusercontent.com/carvel-dev/imgpkg/develop/README.md) — Referência oficial de recursos do Carvel imgpkg especificando ImagesLock, BundleLock, Nested Bundles recursivos e Locations OCI Image; consultado em 2026-10-03.
- [Carvel imgpkg — Official GitHub Repository](https://github.com/carvel-dev/imgpkg) — Repositório oficial Apache-2.0 do Carvel imgpkg; consultado em 2026-10-03.
