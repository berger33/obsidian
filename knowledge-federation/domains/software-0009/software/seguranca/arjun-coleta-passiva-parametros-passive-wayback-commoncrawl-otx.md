---
id: software.seguranca.tranche09.000874
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/s0md3v/Arjun/master/README.md", "https://raw.githubusercontent.com/s0md3v/Arjun/master/arjun/__main__.py", "https://github.com/s0md3v/Arjun/wiki/How-Arjun-works%3F"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arjun **`--passive`**: Extração Passiva de Parâmetros Históricos do **Wayback Machine, CommonCrawl e AlienVault OTX** combinada com Validação Ativa

## Em uma frase
Muitas vezes, uma empresa utiliza nomes de parâmetros internos muito específicos do seu domínio de negócio (`cod_convenio_bacen`, `id_filial_legado`, `token_parceiro_b2b`) que não constam em nenhuma wordlist genérica, mas que já apareceram anos atrás em URLs públicas indexadas pelo **Wayback Machine (Web Archive)**, **CommonCrawl** ou **AlienVault Open Threat Exchange (OTX)**!

## Por que importa
Quando você passa a flag **`--passive`** (ou `--passive exemplo.com.br` para buscar em outro domínio da mesma empresa), a função `fetch_params(host)` do Arjun consulta passivamente essas três fontes de inteligência histórica, extrai todos os nomes de parâmetros únicos que já existiram naquele domínio e **os adiciona automaticamente à wordlist em memória antes de rodar a validação no endpoint alvo**!

## Como funciona
Isso une o histórico OSINT de anos do domínio com a confirmação ativa de busca binária do Arjun!

## Exemplo
```bash
# Coletar nomes de parametros historicos do dominio em fontes OSINT (--passive) e testa-los no endpoint atual com wordlist media
arjun -u https://api.internal.corp/v2/checkout \
  --passive exemplo.com.br \
  -w medium \
  -m GET \
  -oJ /cases/pentest/arjun_passive_enriched.json
```

## Limites e trade-offs
Observe a flag **`-w` (`wordlist`)**: além de aceitar o caminho para qualquer arquivo `.txt` no disco, o Arjun aceita os três atalhos embutidos **`-w large`** (`db/large.txt`, 25.890 parâmetros, padrão), **`-w medium`** (`db/medium.txt`, ~10.000 parâmetros) e **`-w small`** (`db/small.txt`, ~2.000 parâmetros mais frequentes para testes ultrarrápidos)!

## Como verificar
Combine `-w small --passive` quando quiser um scan de apenas 15 requisições que priorize os parâmetros reais que já foram vistos historicamente naquele domínio.

## Conexões
- [[arjun-metodos-http-get-post-json-xml-include-parametros-fixos]] — Veja também: Arjun (`-m GET|POST|JSON|XML` e `--include`): Descoberta de Atributos Ocultos em **APIs REST JSON (**Mass Assignment / BOPLA**)** e Payloads XML.
- [[arjun-conversao-estilo-nomenclatura-casing-camel-snake-kebab]] — Veja também: Arjun **`--casing`**: Adaptação Automática da Wordlist às Convenções de Código do Backend (`snake_case`, `camelCase`, `kebab-case`, `lowercase`).
- [[arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias]] — Referência cruzada direta com arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias.
- [[amass-enumeracao-passiva-ativa-normal-ciclo-dns-certificados]] — Referência cruzada direta com amass-enumeracao-passiva-ativa-normal-ciclo-dns-certificados.

## Fontes
- [Arjun Official GitHub — HTTP Parameter Discovery Suite](https://raw.githubusercontent.com/s0md3v/Arjun/master/README.md) — repositório oficial do Arjun cobrindo descoberta de parâmetros HTTP ocultos e suporte a GET/POST/JSON/XML; consultado em 2026-10-03.
- [Arjun Official Core Source (`arjun/__main__.py`) — Binary Search Narrower, Anomaly Calibration & CLI Flags](https://raw.githubusercontent.com/s0md3v/Arjun/master/arjun/__main__.py) — código-fonte oficial do motor do Arjun mostrando a calibração dos fatores de anomalia (`define`/`compare`), busca binária em chunks e flags CLI; consultado em 2026-10-03.
- [Arjun Official Wiki — How Arjun Works & Usage Guide](https://github.com/s0md3v/Arjun/wiki/How-Arjun-works%3F) — wiki técnica oficial do projeto Arjun detalhando o algoritmo de detecção de anomalias, extração heurística e coleta passiva; consultado em 2026-10-03.
