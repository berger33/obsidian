---
id: software.seguranca.tranche16.001528
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/README.md", "https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/docs/fuzzing_in_depth.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Fuzzing Consciente de Estrutura (**Structure-Aware / Grammar Fuzzing**) no AFL++: **Custom Mutators em C e Python (`AFL_CUSTOM_MUTATOR_LIBRARY` / `PYTHONPATH`)**

## Em uma frase
O que acontece quando o formato de entrada exigido pelo alvo é um **Protobuf binário**, uma **árvore AST complexa**, um **arquivo comprimido `zlib`** ou um protocolo em que 99% das mutações de bits aleatórias corrompem a estrutura externa antes de chegar à lógica de negócio interna?

## Por que importa
Você escreve um **Custom Mutator (`Mutador Customizado`)** em **Python** ou **C/C++** (ou usa bibliotecas prontas como `libprotobuf-mutator` e `Grammar-Mutator`)!

## Como funciona
No AFL++, criar um mutador customizado em Python leva menos de 20 linhas: basta definir as funções **`init(seed)`** e **`fuzz(buf, add_buf, max_size)`** em um arquivo `meu_mutador.py` (que descomprime/parseia o `buf`, aplica uma mutação válida na estrutura interna e serializa/recomprime de volta!) e exportá-lo com **`PYTHONPATH=. AFL_PYTHON_MODULE=meu_mutador`**!

## Exemplo
```python
# Exemplo de Custom Mutator em Python para o AFL++ que garante que todo caso de teste mutado mantenha um cabecalho CRC32 valido nos primeiros 4 bytes
import struct
import zlib

def init(seed):
    pass

def fuzz(buf, add_buf, max_size):
    payload = bytes(buf[4:]) if len(buf) > 4 else b"INIT"
    crc = zlib.crc32(payload) & 0xFFFFFFFF
    out = struct.pack("<I", crc) + payload
    return bytearray(out[:max_size])
```

## Limites e trade-offs
Olhe a função **`fuzz(buf, add_buf, max_size)`** (ou a função adicional **`post_process(buf)`** do AFL++ que é chamada imediatamente antes de enviar qualquer caso de teste gerado pelo próprio AFL++ para o programa alvo!): se o programa alvo rejeita qualquer arquivo cujo `CRC32` nos primeiros 4 bytes não bata com o resto do payload, basta implementar **`post_process(buf)`** recalculando os 4 bytes de `zlib.crc32` em tempo real — assim **100% das mutações geradas pelo AFL++ terão um checksum CRC32 matematicamente perfeito**!

## Como verificar
Se você quiser que o AFL++ use **apenas** o seu mutador customizado (desativando os estágios de mutação de bits padrão), defina também **`export AFL_CUSTOM_MUTATOR_ONLY=1`**.

## Conexões
- [[aflplusplus-fuzzing-binarios-fechados-frida-mode-qemu-unicorn-nyx]] — Veja também: Fuzzing de Binários Sem Código-Fonte (**Binary-Only Targets**) no AFL++: **FRIDA Mode (`-O`)**, **QEMU Mode (`-Q`)**, **Unicorn Mode (`-U`)** e **Nyx Full-System (`-X`)**.
- [[aflplusplus-fuzzing-servicos-rede-desocketing-preeny-afl-network-proxy]] — Veja também: Como Fazer Fuzzing de **Servidores de Rede (TCP/UDP Sockets)** no AFL++: *Desocketing* com `LD_PRELOAD` (`libdesock`), Persistent Harness e Isolamento de Estado.
- [[aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard]] — Referência cruzada direta com aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard.
- [[aflplusplus-instrumentacao-cmplog-redqueen-laf-intel-allowlist-seletiva]] — Referência cruzada direta com aflplusplus-instrumentacao-cmplog-redqueen-laf-intel-allowlist-seletiva.
- [[scapy-fuzzing-protocolos-fuzz-randfield-teste-robustez-parsers-ids]] — Referência cruzada direta com scapy-fuzzing-protocolos-fuzz-randfield-teste-robustez-parsers-ids.

## Fontes
- [AFL++ Official GitHub Repository (`AFLplusplus/AFLplusplus`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/README.md) — repositório oficial do fuzzer guiado por cobertura AFL++ cobrindo `afl-cc`, `afl-fuzz`, análise de cobertura e reprodução de crashes; consultado em 2026-10-03.
- [AFL++ Official In-Depth Fuzzing Guide (`docs/fuzzing_in_depth.md`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/docs/fuzzing_in_depth.md) — guia técnico oficial do AFL++ detalhando modos `LTO`/`LLVM`/`GCC_PLUGIN`, `AFL_LLVM_CMPLOG=1`, `AFL_LLVM_LAF_ALL=1`, `AFL_LLVM_ALLOWLIST`, Persistent Mode, `afl-cmin`/`afl-tmin` e campanhas multicore; consultado em 2026-10-03.
