---
id: software.devops.tranche16.001521
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
fontes: ["https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md", "https://carvel.dev/kbld/docs/v0.44.x/config/", "https://github.com/carvel-dev/kbld"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel kbld: resolução de referências de imagens para digests imutáveis SHA-256 e anotações de rastreabilidade

## Em uma frase
O Carvel `kbld` (`kei·bild`, CNCF Carvel) localiza referências de imagens de container em manifestos YAML, orquestra builds ou consultas a registries OCI e substitui tags mutáveis (como `:v1.2.0` ou `:latest`) por referências imutáveis baseadas em digest (`@sha256:...`).

## Por que importa
Implantar em produção usando tags mutáveis (`image: app:1.0`) quebra a reprodutibilidade e abre brechas de segurança: se a tag for sobrescrita no registry, novos Pods escalados pelo HPA executarão um binário diferente dos Pods antigos sem que o manifesto Git tenha mudado.

## Como funciona
Ao processar `kbld -f manifestos.yml`, a ferramenta resolve cada imagem contra o registry (ou executa o build local configurado), reescreve o campo `image:` para o formato `repo@sha256:<digest>` e anexa no recurso Kubernetes a anotação `kbld.k14s.io/images` contendo um relatório YAML com a tag original, o digest resolvido e metadados da origem Git ou do builder.

## Exemplo
```bash
kbld -f deployment.yml > deployment-resolved.yml
grep -E "image:|kbld.k14s.io/images" deployment-resolved.yml
```

## Limites e trade-offs
O `kbld` consome e remove da saída todos os documentos `apiVersion: kbld.k14s.io/v1alpha1` (`kind: Config`), emitindo apenas os manifestos da aplicação prontos para serem aplicados pelo `kapp` ou `kubectl`.

## Como verificar
Inspecione o manifesto de saída `deployment-resolved.yml` e confirme que todas as chaves `image:` contêm `@sha256:` de 64 caracteres hexadecimais e que a anotação `kbld.k14s.io/images` documenta a resolução.

## Conexões
- [[carvel-kbld-config-search-rules-keymatcher-valuematcher]] — Veja também: Carvel kbld: configuração de `searchRules` com `keyMatcher` e `valueMatcher`.

## Fontes
- [Carvel kbld GitHub — README.md (Image Building Orchestration, Immutable Digest Resolution & Resource Metadata Annotations)](https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md) — README oficial do carvel-dev/kbld descrevendo orquestração de builds, resolução de imagens para digests SHA-256 e anotações de metadados; consultado em 2026-10-03.
- [Carvel kbld Official Documentation — Configuration v0.44.x (searchRules, keyMatcher, valueMatcher, updateStrategy, overrides, sources & destinations)](https://carvel.dev/kbld/docs/v0.44.x/config/) — Especificação oficial do objeto Config (kbld.k14s.io/v1alpha1) detalhando searchRules, parse recursivo de YAML/JSON em ConfigMaps, sources, destinations e overrides; consultado em 2026-10-03.
- [Carvel kbld — Official GitHub Repository](https://github.com/carvel-dev/kbld) — Repositório oficial Apache-2.0 do Carvel kbld; consultado em 2026-10-03.
