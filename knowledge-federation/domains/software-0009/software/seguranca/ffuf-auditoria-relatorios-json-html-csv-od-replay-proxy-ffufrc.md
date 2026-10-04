---
id: software.seguranca.tranche04.000340
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/ffuf/ffuf/master/README.md", "https://raw.githubusercontent.com/ffuf/ffuf/master/ffufrc.example", "https://github.com/ffuf/ffuf/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# ffuf: Padronização com `ffufrc` (`-config`), Artefatos de Resposta (`-od`), Relatórios (`-of all`) e `-replay-proxy`

## Em uma frase
O `ffuf` suporta perfis declarativos TOML (`$XDG_CONFIG_HOME/ffuf/ffufrc` ou `-config`), gravação completa de cabeçalhos e corpos das respostas encontradas (`-od`), múltiplos formatos de relatório (`-of json|ejson|html|md|csv|all`) e `-replay-proxy`.

## Por que importa
Garante rastreabilidade forense durante testes de segurança: cada achado fica registrado em JSON/HTML com o corpo bruto salvo em disco (`-od`) e reenviado opcionalmente a um proxy de auditoria (ZAP, Caido ou Burp) via `-replay-proxy`.

## Como funciona
Diferente da flag `-x` (que envia **todo** o tráfego ruidoso da wordlist pelo proxy, degradando a performance), a flag `-replay-proxy http://127.0.0.1:8080` envia pelo proxy **exclusivamente** as requisições que passaram pelos *matchers* e *filters*. Já `-or` (*output required*) evita criar arquivos de relatório vazios quando nenhum endpoint é encontrado.

## Exemplo
```bash
# Executar scan usando perfil TOML corporativo, salvando relatórios e replay apenas dos matches
ffuf -config /etc/security/ffufrc-staging.toml \
  -w /usr/share/seclists/Discovery/Web-Content/api-endpoints.txt \
  -u https://api.staging.corp/FUZZ \
  -o /tmp/ffuf-results/scan-api -of all -or \
  -od /tmp/ffuf-results/raw-bodies \
  -replay-proxy http://127.0.0.1:8080
```

## Limites e trade-offs
Ao usar um arquivo `ffufrc` padrão em `~/.config/ffuf/ffufrc`, lembre-se de que flags repetíveis como `-H` passadas na linha de comando são **concatenadas** às do arquivo de configuração em vez de substituí-las.

## Como verificar
Verifique `/tmp/ffuf-results/scan-api.json` com `jq '.results | length'` e confirme que o diretório `-od` contém apenas os pares request/response das URLs validadas.

## Conexões
- [[ffuf-mutadores-externos-input-cmd-radamsa-ffuf-num]] — Veja também: ffuf: Geração Dinâmica de Payloads e Fuzzing Mutacional com `--input-cmd`, `--input-num` e `$FFUF_NUM`.
- [[ffuf-arquitetura-web-fuzzer-go-keyword-fuzz-diretorios-arquivos]] — Referência cruzada direta com ffuf-arquitetura-web-fuzzer-go-keyword-fuzz-diretorios-arquivos.
- [[ffuf-rate-limiting-threads-delay-stop-flags-sa-sf-se-interativo]] — Referência cruzada direta com ffuf-rate-limiting-threads-delay-stop-flags-sa-sf-se-interativo.
- [[ffuf-fuzzing-parametros-get-post-json-headers-raw-request]] — Referência cruzada direta com ffuf-fuzzing-parametros-get-post-json-headers-raw-request.

## Fontes
- [ffuf GitHub — README.md (Fast Web Fuzzer in Go, Content/Vhost/Parameter/POST Fuzzing, Matchers, Filters & Interactive Mode)](https://raw.githubusercontent.com/ffuf/ffuf/master/README.md) — README oficial do ffuf/ffuf documentando todos os modos de operação, flags de matcher/filter, auto-calibração, recursão e mutadores externos; consultado em 2026-10-03.
- [ffuf GitHub — ffufrc.example (Declarative TOML Configuration Reference for HTTP, General, Input, Output, Filter & Matcher Sections)](https://raw.githubusercontent.com/ffuf/ffuf/master/ffufrc.example) — Arquivo oficial de exemplo de configuração ffufrc detalhando todas as opções declarativas do ffuf; consultado em 2026-10-03.
- [ffuf Official Wiki — Advanced Usage & Configuration Guide](https://github.com/ffuf/ffuf/wiki) — Documentação oficial da wiki do projeto ffuf; consultado em 2026-10-03.
