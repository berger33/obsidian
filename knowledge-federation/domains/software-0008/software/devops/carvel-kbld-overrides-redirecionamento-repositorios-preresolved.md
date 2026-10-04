---
id: software.devops.tranche16.001526
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
fontes: ["https://carvel.dev/kbld/docs/v0.44.x/config/", "https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md", "https://github.com/carvel-dev/kbld"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel kbld: redirecionamento de imagens e pré-resolução offline via `overrides`

## Em uma frase
A seção `overrides` da configuração do `kbld` permite substituir referências de imagem encontradas nos manifestos de entrada por novos endereços (`newImage`) antes da etapa de resolução ou build, incluindo a opção `preresolved: true` para ambientes sem acesso ao registry no momento do render.

## Por que importa
Quando um manifesto upstream referencia `nginx:1.25` (no Docker Hub) mas a política corporativa exige puxar de um espelho interno (`registry.corp.internal/mirror/nginx:1.25`) ou fixar um digest já conhecido sem realizar chamadas de rede na máquina de build, `overrides` resolve o problema declarativamente.

## Como funciona
O `kbld` aplica a lista de `overrides` logo após identificar as referências pelas `searchRules`. Se `preresolved: true` for definido na regra de override, o `kbld` aceita `newImage` exatamente como informada (por exemplo, já contendo `@sha256:...`) sem consultar nenhum servidor de registry remoto nem invocar builders.

## Exemplo
```yaml
apiVersion: kbld.k14s.io/v1alpha1
kind: Config
overrides:
  - image: nginx:1.25
    newImage: registry.corp.internal/library/nginx@sha256:4c0fdaa8b6341bfdeca5f18f7837462c80cff90527ee35ef185571e1c327beac
    preresolved: true
```

## Limites e trade-offs
Se `preresolved: true` for usado com uma referência que ainda utiliza tag mutável em vez de `@sha256:...`, o manifesto emitido perderá a garantia de imutabilidade criptográfica normalmente assegurada pelo `kbld`.

## Como verificar
Execute `kbld -f deployment.yml -f kbld-overrides.yml` com a rede desconectada e confirme que a imagem `nginx:1.25` é substituída instantaneamente sem tentativa de conexão externa.

## Conexões
- [[carvel-kbld-destinations-publicacao-registries-remotos]] — Veja também: Carvel kbld: publicação automática de imagens construídas em registries OCI via `destinations`.
- [[carvel-kbld-lock-output-imgpkg-imageslock-geracao]] — Veja também: Carvel kbld: geração de arquivos de lock (`--lock-output` e `--imgpkg-lock-output`) para reprodutibilidade.

## Fontes
- [Carvel kbld GitHub — README.md (Image Building Orchestration, Immutable Digest Resolution & Resource Metadata Annotations)](https://carvel.dev/kbld/docs/v0.44.x/config/) — README oficial do carvel-dev/kbld descrevendo orquestração de builds, resolução de imagens para digests SHA-256 e anotações de metadados; consultado em 2026-10-03.
- [Carvel kbld Official Documentation — Configuration v0.44.x (searchRules, keyMatcher, valueMatcher, updateStrategy, overrides, sources & destinations)](https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md) — Especificação oficial do objeto Config (kbld.k14s.io/v1alpha1) detalhando searchRules, parse recursivo de YAML/JSON em ConfigMaps, sources, destinations e overrides; consultado em 2026-10-03.
- [Carvel kbld — Official GitHub Repository](https://github.com/carvel-dev/kbld) — Repositório oficial Apache-2.0 do Carvel kbld; consultado em 2026-10-03.
