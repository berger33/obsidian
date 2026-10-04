---
id: software.seguranca.tranche13.001240
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/mandiant/flare-floss/master/README.md", "https://raw.githubusercontent.com/mandiant/flare-floss/master/doc/usage.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Automação em Lote com o **FLOSS** (`FLOSS_CACHE_DIR`, API JSON) para Triagem de Malware em Escala e Auditoria de Binários de Terceiros

## Em uma frase
Em operações de **SOC / CSIRT**, **Threat Intelligence** ou **Auditoria de Segurança de Software de Terceiros (Supply Chain)**, muitas vezes é necessário analisar dezenas de binários de uma só vez (por exemplo, todos os executáveis e DLLs coletados de uma pasta `C:\ProgramData\` comprometida, ou todos os binários de uma atualização de fornecedor).

## Por que importa
Sem cache de resultados e saída estruturada JSON, reprocessar bibliotecas compartilhadas idênticas em múltiplos diretórios desperdiçaria ciclos de emulação de CPU.

## Como funciona
Configurando a variável de ambiente **`FLOSS_CACHE_DIR`** (que armazena automaticamente os resultados JSON indexados pelo hash `SHA-256` de cada binário analisado para nunca reprocessar o mesmo arquivo duas vezes!) e combinando `floss -j -q` com **`jq`**, você pode construir em poucas linhas um pipeline de triagem que extrai automaticamente todas as **URLs, IPs, chaves de registro, caminhos de arquivos e strings decodificadas** de uma pasta inteira de amostras suspeitas!

## Exemplo
```bash
# Processar uma pasta de binarios suspeitos em lote usando cache SHA-256 automatico (FLOSS_CACHE_DIR) e consolidar URLs/IPs/Decoded Strings
export FLOSS_CACHE_DIR="./.floss_cache"
mkdir -p "$FLOSS_CACHE_DIR" ./relatorios_floss
for bin in ./coleta_ir/*.exe; do
  [ -f "$bin" ] || continue
  nome=$(basename "$bin")
  floss -q -j "$bin" > "./relatorios_floss/${nome}.floss.json"
done
jq -r '(.strings.decoded_strings[]?.string), (.strings.stack_strings[]?.string)' ./relatorios_floss/*.floss.json | sort -u
```

## Limites e trade-offs
Esse comando final com `jq` lista instantaneamente, sem duplicatas (`sort -u`), **todas as strings que qualquer um dos binários coletados tentou esconder via Stack Strings ou Decoded Strings**!

## Como verificar
Combine esse pipeline com a verificação do **Mandiant `capa`** (`capa -q -j`) sobre a mesma pasta `./coleta_ir/` para obter em poucos minutos um inventário completo de capacidades comportamentais + strings desofuscadas de todo o incidente.

## Conexões
- [[floss-criacao-regras-yara-ioc-hunting-a-partir-strings-desofuscadas]] — Veja também: Armadilha Clássica em **Regras YARA**: Por que Usar *Decoded Strings* do FLOSS em Regras YARA de Disco Falha (e Como Usar para Caça em Memória!).
- [[floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded]] — Referência cruzada direta com floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded.
- [[floss-busca-filtragem-query-regex-json-html-web-viewer]] — Referência cruzada direta com floss-busca-filtragem-query-regex-json-html-web-viewer.
- [[capa-workflow-combinado-floss-yara-velociraptor-engenharia-reversa]] — Referência cruzada direta com capa-workflow-combinado-floss-yara-velociraptor-engenharia-reversa.

## Fontes
- [Mandiant FLARE Obfuscated String Solver (`flare-floss`) Official GitHub](https://raw.githubusercontent.com/mandiant/flare-floss/master/README.md) — repositório oficial do Mandiant FLOSS cobrindo extração de strings estáticas conscientes de layout, stack strings, tight strings, decoded strings e binários Go/Rust; consultado em 2026-10-03.
- [Mandiant FLOSS Official Usage Guide (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/flare-floss/master/doc/usage.md) — documentação oficial de opções avançadas do FLOSS (`--only`, `--no`, `--functions`, `--section`, `--structure`, `--tag`, `--interesting`, `--query`, `--html`, `-L` e `FLOSS_CACHE_DIR`); consultado em 2026-10-03.
