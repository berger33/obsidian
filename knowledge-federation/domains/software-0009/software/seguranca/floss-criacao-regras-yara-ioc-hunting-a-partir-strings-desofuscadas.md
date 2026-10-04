---
id: software.seguranca.tranche13.001239
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

# Armadilha Clássica em **Regras YARA**: Por que Usar *Decoded Strings* do FLOSS em Regras YARA de Disco Falha (e Como Usar para Caça em Memória!)

## Em uma frase
Aqui está uma das armadilhas técnicas mais importantes na interseção entre **FLOSS** e **YARA**, na qual muitos analistas juniores caem: você roda o `floss amostra.exe`, descobre na seção **`FLOSS DECODED STRINGS`** uma string única incrível como `"Mutex_APT_Secret_2026"`, coloca essa string como `$s1 = "Mutex_APT_Secret_2026"` dentro de uma regra **YARA** e roda `yara regra.yar amostra.exe` no arquivo em disco... **e a regra YARA NÃO DÁ MATCH!** Por que isso aconteceu?

## Por que importa
Porque uma **Decoded String** ou **Stack String** extraída pelo FLOSS **não existe em texto claro nos bytes estáticos do arquivo em disco**! No disco, a *Decoded String* está cifrada (ex.: em XOR/RC4) e só passa a existir em texto claro **na memória RAM do processo após a função de decodificação rodar**; e a *Stack String* está quebrada em várias instruções `mov byte ptr [rbp-XX], ...`!

## Como funciona
Portanto, siga esta regra de ouro ao criar regras **YARA** a partir da saída do FLOSS: **(1) Para varrer arquivos estáticos em disco**, use na regra YARA as **Static Strings / Go-Rust Strings** do FLOSS + os **bytes/opcodes da função de decodificação (`address` mostrada pelo `floss -v`)**; e **(2) Use as `Decoded Strings` na regra YARA especificamente para varrer a MEMÓRIA RAM dos processos em execução (`yara regra.yar <PID>`, Velociraptor `Windows.Detection.Yara.Process` ou Volatility `yarascan`)**, onde a string já foi descriptografada pelo malware!

## Exemplo
```bash
# Inspecionar com floss -v os enderecos de funcoes das Stack/Decoded Strings para extrair opcodes estaticos ou caçar a string limpa na RAM
floss --only stack tight decoded -v ./amostras/apt_implant.exe
```

## Limites e trade-offs
Compreender essa distinção entre **artefato estático em disco** e **artefato dinâmico desofuscado em memória** separa imediatamente o analista sênior de malware: com o FLOSS, você obtém tanto o endereço da rotina de ofuscação (para detectar o arquivo cifrado no disco via opcodes YARA) quanto a string decodificada (para detectar o processo injetado na memória RAM via EDR/Velociraptor)!

## Como verificar
Para *Stack Strings* simples, você também pode capturar a sequência de bytes das instruções `mov` no endereço da função apontado pelo `floss -v` usando curingas nos offsets de pilha da regra YARA.

## Conexões
- [[floss-analise-shellcode-arquivos-grandes-limites-tuning-performance]] — Veja também: Analisando **Shellcodes (`-f sc32`/`sc64`)** e Binários Gigantes (**`-L` / `--large-file`**, `--max-strings`, `--max-address-space`) no FLOSS.
- [[floss-automacao-python-batch-triage-comparacao-builds-supply-chain]] — Veja também: Automação em Lote com o **FLOSS** (`FLOSS_CACHE_DIR`, API JSON) para Triagem de Malware em Escala e Auditoria de Binários de Terceiros.
- [[floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded]] — Referência cruzada direta com floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded.
- [[capa-workflow-combinado-floss-yara-velociraptor-engenharia-reversa]] — Referência cruzada direta com capa-workflow-combinado-floss-yara-velociraptor-engenharia-reversa.

## Fontes
- [Mandiant FLARE Obfuscated String Solver (`flare-floss`) Official GitHub](https://raw.githubusercontent.com/mandiant/flare-floss/master/README.md) — repositório oficial do Mandiant FLOSS cobrindo extração de strings estáticas conscientes de layout, stack strings, tight strings, decoded strings e binários Go/Rust; consultado em 2026-10-03.
- [Mandiant FLOSS Official Usage Guide (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/flare-floss/master/doc/usage.md) — documentação oficial de opções avançadas do FLOSS (`--only`, `--no`, `--functions`, `--section`, `--structure`, `--tag`, `--interesting`, `--query`, `--html`, `-L` e `FLOSS_CACHE_DIR`); consultado em 2026-10-03.
